from typing import Mapping, Optional

import pytest
from beet import DataPack, Function, ResourcePack

from lectern import Directive, Document, Fragment, InvalidFragment


def test_empty():
    assert Document() == Document()
    assert Document().data == DataPack()
    assert Document().assets == ResourcePack()
    assert Document().get_text() == ""
    empty = "# Lectern snapshot\n\nThe data pack and resource pack are empty.\n"
    assert Document().get_markdown() == empty
    assert Document().get_markdown(emit_external_files=True) == (empty, {})
    assert Document(text="Nothing to see here") == Document()
    assert Document(markdown="Nothing to see here") == Document()


def test_data_pack():
    pack = DataPack()
    doc = Document(data=pack)
    assert doc.data is pack


def test_resource_pack():
    pack = ResourcePack()
    doc = Document(assets=pack)
    assert doc.assets is pack


def test_text_basic():
    source = "@function demo:foo\nsay hello\n"
    assert source in Document(text=source).get_text()


def test_text_function():
    pack = DataPack()
    pack["demo:foo"] = Function(["say foo"])

    doc = Document(data=pack)
    doc.add_text("@function demo:bar\nsay bar\n")

    assert pack.functions == {
        "demo:foo": Function(["say foo"]),
        "demo:bar": Function(["say bar"]),
    }


def test_text_tricky():
    doc = Document(
        text="some preamble\n\n"
        "@function demo:foo\n"
        "say foo\n"
        "@other_thing hello world\n"
        "say after\n"
        " @function not taken into account\n"
        "say next\n"
        "@function demo:bar\n"
        "say bar\n"
    )
    assert len(doc.data.functions) == 2


def test_markdown_breaks():
    doc = Document()
    doc.directives["dummy"] = lambda fragment, _, data: data.functions.update(
        {fragment.expect("full_name"): Function(["say dummy"])}
    )
    doc.add(
        "same paragraph\n`@dummy demo:dummy`\n`@function demo:foo`\n```\nsay foo\n```\n"
    )
    assert doc.data.functions == {
        "demo:dummy": Function(["say dummy"]),
        "demo:foo": Function(["say foo"]),
    }


def test_missing_argument():
    with pytest.raises(
        InvalidFragment, match="Missing argument 'full_name' for directive @function."
    ):
        Document(text="@function\nsay hello")


def test_extra_argument():
    with pytest.raises(
        InvalidFragment, match="Unexpected argument 'banana' for directive @function."
    ):
        Document(text="@function demo:foo banana\nsay hello")


def test_no_content():
    with pytest.raises(
        InvalidFragment, match="Expected content, path or url for directive @function."
    ):
        Document(markdown="`@function demo:foo`\n")


def test_loader():
    def handle_ignore_modifier(
        fragment: Fragment, directives: Mapping[str, Directive]
    ) -> Optional[Fragment]:
        if fragment.modifier == "ignore":
            return None
        return fragment

    document = Document()
    document.loaders.append(handle_ignore_modifier)
    document.add_text("@function(ignore) demo:foo\nsay hello")
    assert not document.data
