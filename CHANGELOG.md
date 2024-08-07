# Changelog

<!--next-version-placeholder-->

## v0.34.0 (2024-07-21)

### Feature

* Update beet ([`a5e7980`](https://github.com/mcbeet/lectern/commit/a5e798066aef91937b31d89d1e2ff365acd06dcf))

## v0.33.0 (2024-03-29)

### Feature

* Add lectern.contrib.tagged_function_shorthand ([`3ea2017`](https://github.com/mcbeet/lectern/commit/3ea201743f48b0614a9c5de2d7af5b91e0ca3995))

## v0.32.0 (2023-12-17)

### Feature

* Add error message when detecting badly formatted code blocks ([`025f4bb`](https://github.com/mcbeet/lectern/commit/025f4bb246b934978e9631d741df5f000654525c))
* Allow multiple directives in a paragraph ([`d43f32e`](https://github.com/mcbeet/lectern/commit/d43f32e83e090a012075cb11d434016251f720bb))

### Fix

* Don't enforce argument names for directive protocol ([`a62a015`](https://github.com/mcbeet/lectern/commit/a62a015072eebe400a54482aa3c8a6bcb3418c40))

## v0.31.0 (2023-12-06)

### Feature

* Bump pack format ([`5d1818b`](https://github.com/mcbeet/lectern/commit/5d1818bf1f747745d94f0379ca86126bc887aa44))

## v0.30.0 (2023-12-02)

### Feature

* Add lectern.contrib.vanilla ([`c21e95d`](https://github.com/mcbeet/lectern/commit/c21e95d53be51cc4ba8b34922d581270570ca245))

## v0.29.2 (2023-10-24)

### Fix

* Extract overlay with relative path ([`e7be328`](https://github.com/mcbeet/lectern/commit/e7be328fd19e1a6f2e03f2d3498cd6375363404a))

## v0.29.1 (2023-10-09)

### Fix

* Handle missing directive ([`d88289f`](https://github.com/mcbeet/lectern/commit/d88289ff3f8aec6c22e9091796f668ea3144d4cb))

## v0.29.0 (2023-10-09)

### Feature

* Support overlays ([`518f3c9`](https://github.com/mcbeet/lectern/commit/518f3c993046fef9f9c35cb7e8fa7d23757ff949))

## v0.28.0 (2023-08-07)

### Feature

* Apply directives to context directly ([`a4cbf48`](https://github.com/mcbeet/lectern/commit/a4cbf48639fb553f2897adec049f47038d651b9c))

## v0.27.1 (2023-08-06)

### Fix

* Don't emit fallback function if there are fragments ([`57c8c0f`](https://github.com/mcbeet/lectern/commit/57c8c0f2397a5723a5baa969475dc0f9e25bd48e))

## v0.27.0 (2023-08-06)

### Feature

* Shorthand ([`6717332`](https://github.com/mcbeet/lectern/commit/6717332d9facf92f3d58c8e6c62d2b58712c96a0))

## v0.26.0 (2022-10-25)
### Feature
* Add merge_zip directive ([`add74f2`](https://github.com/mcbeet/lectern/commit/add74f2f8b223b29f2270de3aec5205ff217944d))

## v0.25.0 (2022-09-20)
### Feature
* Make it possible to raise an error if there was nothing in the message ([`165330e`](https://github.com/mcbeet/lectern/commit/165330e29e490860107d2755f09a0aa3f9d9c03a))

## v0.24.1 (2022-09-17)
### Fix
* Don't add namespace title when the namespace is empty ([`adfa7e5`](https://github.com/mcbeet/lectern/commit/adfa7e5493d4fc05df2e771c59f8e455c4e239c2))
* Properly convert serialized content ([`3301864`](https://github.com/mcbeet/lectern/commit/3301864338413427ac7ab14e6aa0b7fb0e56d55f))

## v0.24.0 (2022-06-18)
### Feature
* Change serialization filter for pytest snapshots ([`aea38cf`](https://github.com/mcbeet/lectern/commit/aea38cfd2db89b8d4470fa0805b54b5e2752d231))

## v0.23.0 (2022-06-18)
### Feature
* Add serialization pack filter ([`c841d6b`](https://github.com/mcbeet/lectern/commit/c841d6b6eb7dea115c3d2a791f36cca672362aaf))

## v0.22.0 (2022-06-18)
### Feature
* Update beet to default to 1.19 ([`4f2f2e9`](https://github.com/mcbeet/lectern/commit/4f2f2e901dbe6f80f5b000e2ee6abe78546b9f96))

## v0.21.2 (2022-04-29)
### Fix
* Don't do fancy concatenation ([`8d7dd36`](https://github.com/mcbeet/lectern/commit/8d7dd367553524ca061e92edb6c78f9f0fd4ce4c))

## v0.21.1 (2022-04-29)
### Fix
* Use packageable paths ([`8e42a07`](https://github.com/mcbeet/lectern/commit/8e42a075649db47c6165749e594e331b46c819f6))

## v0.21.0 (2022-04-29)
### Feature
* Add LinkFragmentLoader ([`9d2980c`](https://github.com/mcbeet/lectern/commit/9d2980cbcb439ce8b5218c75abc6c8299222ab0f))
* Add lectern.contrib.messaging ([`e94e460`](https://github.com/mcbeet/lectern/commit/e94e460f882b421b97c4108c583a7a11ecfd2886))

### Fix
* Return bool to indicate if files were added ([`6ae62bd`](https://github.com/mcbeet/lectern/commit/6ae62bd50917ab8da2d1da86258d3ef3bc183a18))

## v0.20.1 (2022-04-26)
### Fix
* Use BubbleException ([`d2ded22`](https://github.com/mcbeet/lectern/commit/d2ded223f3c65d1ebf98daee56d69881e0e83140))

## v0.20.0 (2022-04-06)
### Feature
* Add format sniffer and allow regular text format in code blocks ([`85420af`](https://github.com/mcbeet/lectern/commit/85420afe3ef856f570c4583936a606d824cbff2a))

### Fix
* Update pyright ([`919657c`](https://github.com/mcbeet/lectern/commit/919657cbb6d10ddb80020b1dd581504ac87c3fa6))
* Update dependencies ([`811b833`](https://github.com/mcbeet/lectern/commit/811b8337d8383a593e314e3cc68a1511386421a4))

## v0.19.1 (2022-03-01)
### Fix
* Use compatible beet dependency specifier ([`5eb9d1b`](https://github.com/mcbeet/lectern/commit/5eb9d1bc1818e59d832943ae9caa9f4841bb3fe9))

## v0.19.0 (2022-02-28)
### Feature
* Update to 1.18.2 ([`d9e9f16`](https://github.com/mcbeet/lectern/commit/d9e9f16c85e716d0e3eb7f98cfac7f801064b06c))

## v0.18.2 (2021-12-22)
### Fix
* Don't overwrite output pack by default ([`0f9bd42`](https://github.com/mcbeet/lectern/commit/0f9bd42065fd899ed1dbc2c3a9033ea51c06ebdf))

## v0.18.1 (2021-11-29)
### Fix
* Missing blank line in flat format ([`db3c1fc`](https://github.com/mcbeet/lectern/commit/db3c1fcfb9f252cf037ea22c706d6a254d4b0ad3))

## v0.18.0 (2021-11-16)
### Feature
* Add flat markdown ([`45c5cf5`](https://github.com/mcbeet/lectern/commit/45c5cf5d7c949e824936ce43fce346c06b4af8ad))

## v0.17.1 (2021-11-05)
### Fix
* Update list of supported resources ([`fbbbbdc`](https://github.com/mcbeet/lectern/commit/fbbbbdc6a3c96fe0e496e01a8732eadb7ea67485))

## v0.17.0 (2021-11-05)
### Feature
* Add dynamic directive resolvers ([`b2b6d21`](https://github.com/mcbeet/lectern/commit/b2b6d21207bb0645799f5b26413de10d49ed64f0))

## v0.16.1 (2021-10-23)
### Fix
* Update lockfile and add discord badge ([`3a76ee5`](https://github.com/mcbeet/lectern/commit/3a76ee57d1f125359b74d20d673bfa3dc862742c))

## v0.16.0 (2021-09-08)
### Feature
* Add lectern.contrib.plugin ([`17e1c78`](https://github.com/mcbeet/lectern/commit/17e1c7830d73035b561388aece25d85a542057f8))

## v0.15.3 (2021-09-01)
### Fix
* Update dependencies and make pyright happy with new click typings ([`9edd063`](https://github.com/mcbeet/lectern/commit/9edd06327146f065ed348bddebf8aec0d1ea128a))

## v0.15.2 (2021-07-01)
### Fix
* Declare lectern plugin with configurable decorator ([`dbcd46c`](https://github.com/mcbeet/lectern/commit/dbcd46c6c7fd3acc476268576344a60e6095b652))

## v0.15.1 (2021-06-26)
### Fix
* Forgot to document lectern.contrib.yaml_to_json usage in config file ([`97d5cab`](https://github.com/mcbeet/lectern/commit/97d5cabbc9376d141f05dc687647ce49524f01f5))

## v0.15.0 (2021-06-26)
### Feature
* Add lectern.contrib.yaml_to_json plugin ([`9a3ab5e`](https://github.com/mcbeet/lectern/commit/9a3ab5eb30740b3946d765246f3ad40545768989))
* Baked files can now be stored back into fragments ([`430e539`](https://github.com/mcbeet/lectern/commit/430e539e7fcb9496c8245c81159aed9a59f8ec40))
* Rewrite lectern.contrib.relative_location with a fragment loader ([`f26e167`](https://github.com/mcbeet/lectern/commit/f26e1672f42208a257dfea68a081f13e6fd4c809))
* Add fragment loaders ([`c46184a`](https://github.com/mcbeet/lectern/commit/c46184a557438024e604efe5accdb168c9402e05))

## v0.14.0 (2021-06-24)
### Feature
* Add lectern.contrib.relative_location ([`9ce8cff`](https://github.com/mcbeet/lectern/commit/9ce8cff3681b0a54d15cf3db5a8e328d56e80784))

### Fix
* Add type alias for AnyDirective ([`87b73de`](https://github.com/mcbeet/lectern/commit/87b73deea1aab47eeb374100e33ddff8d74a3548))

## v0.13.1 (2021-06-11)
### Fix
* Update logo ([`cafaf65`](https://github.com/mcbeet/lectern/commit/cafaf65ef92c141cc952409fd6962cef1b801a99))

## v0.13.0 (2021-05-09)
### Feature
* Add define directive ([`85ec3cc`](https://github.com/mcbeet/lectern/commit/85ec3ccdd682f35c0e3556e116dab48cb55a27a9))
* Move require and script directives into their own beet plugins ([`a1e33cd`](https://github.com/mcbeet/lectern/commit/a1e33cd1312040794cb11900b0c64ae1835208b5))

### Fix
* Pack.png url now uses a static revision ([`1f7013c`](https://github.com/mcbeet/lectern/commit/1f7013cad5b6bd185322da5fb5880f285df30de5))

## v0.12.0 (2021-05-09)
### Feature
* Clean error message for invalid urls ([`7964d24`](https://github.com/mcbeet/lectern/commit/7964d24ba0991cfa8a8b8d40d426a295075117ae))
* Add script directive ([`81603f9`](https://github.com/mcbeet/lectern/commit/81603f9b845e178d011e66c70f85495dcaaf00ea))
* Add directive escaping ([`5fbd90c`](https://github.com/mcbeet/lectern/commit/5fbd90c8d95a341a56942cd6d4df1e73f4da31b9))
* Add download modifier ([`77f0864`](https://github.com/mcbeet/lectern/commit/77f086407a9393a735bec32fc437e4b45a097893))

## v0.11.1 (2021-04-27)
### Fix
* Serialize namespace extra ([`94f1995`](https://github.com/mcbeet/lectern/commit/94f1995808d9be25c5a604132b99aff7554984ba))

## v0.11.0 (2021-04-27)
### Feature
* Add sound and particle directives ([`87aa5f9`](https://github.com/mcbeet/lectern/commit/87aa5f981bac2db1289ffd55d583e6f5af818108))

## v0.10.1 (2021-04-25)
### Fix
* The snapshot testing example was not using run_beet properly ([`3c933e8`](https://github.com/mcbeet/lectern/commit/3c933e81080a1180b31d2940afca023ac9a7daf3))

## v0.10.0 (2021-04-24)
### Feature
* Add prepend modifier ([`5e1bb1e`](https://github.com/mcbeet/lectern/commit/5e1bb1e81835b8a8aaaedab0f1d2fb138bd3d993))

## v0.9.3 (2021-04-02)
### Fix
* **deps:** Don't use caret to depend on beet because it's not 1.0 yet ([`a97779f`](https://github.com/mcbeet/lectern/commit/a97779fd7bcb22efafeb95b4f383cbd86d61000f))

## v0.9.2 (2021-03-27)
### Fix
* Snapshots shouldn't compare data pack and resource pack names ([`941605b`](https://github.com/mcbeet/lectern/commit/941605b24ef11452e7534af3a7a4bf2597f3f164))

## v0.9.1 (2021-03-24)
### Fix
* Version ranges were weird again ([`bc37fd9`](https://github.com/mcbeet/lectern/commit/bc37fd943021e2d4ab7203f3ac20afb21945d3c4))

## v0.9.0 (2021-03-21)
### Feature
* Update beet and add shader highlighting ([`13e4659`](https://github.com/mcbeet/lectern/commit/13e465995c09a7bc9d974c64e829fca82721fb39))

### Breaking
* `@shader_program` directive renamed to `@shader`  ([`13e4659`](https://github.com/mcbeet/lectern/commit/13e465995c09a7bc9d974c64e829fca82721fb39))

## v0.8.2 (2021-03-19)
### Fix
* Update beet ([`87b0931`](https://github.com/mcbeet/lectern/commit/87b0931c9ec156af4ea468ca27084dd69d92545a))

## v0.8.1 (2021-03-17)
### Fix
* Make the directive comment regex a little more forgiving ([`0471780`](https://github.com/mcbeet/lectern/commit/0471780274e10b3bab2d66d04529af5b269618a4))

## v0.8.0 (2021-03-17)
### Feature
* Add hidden fragments ([`510a213`](https://github.com/mcbeet/lectern/commit/510a2131906257893e23e452dee6336dc38a94eb))

### Fix
* Report line number in error messages ([`c998d68`](https://github.com/mcbeet/lectern/commit/c998d6877c33a91d6ef6a8f9b5cac8dbd0db53dd))
* Take the backticks into account for code fence start line ([`a2c442c`](https://github.com/mcbeet/lectern/commit/a2c442c628ea1087d8f898b9ff504f627070f2f2))

## v0.7.1 (2021-03-09)
### Fix
* Rename get_markdown prefix argument ([`85650fa`](https://github.com/mcbeet/lectern/commit/85650fa930fdeb27b24244b772412e72030b14d3))

## v0.7.0 (2021-03-08)
### Feature
* Add lectern scripts ([`0890b9d`](https://github.com/mcbeet/lectern/commit/0890b9dafd219a4ff9a19698c29def0e1d77e855))
* Add markdown prefetcher ([`e5f65dd`](https://github.com/mcbeet/lectern/commit/e5f65dd0ed01b1066723a176c221627412e12762))
* Add fragment location ([`d79f987`](https://github.com/mcbeet/lectern/commit/d79f987142a1148171cc005aceb6698c2edb564a))
* Enhance pytest explanation ([`8f9b18d`](https://github.com/mcbeet/lectern/commit/8f9b18dbc94e1cd760897826fc30254ad1a4718d))

### Fix
* Accidentally broke emitted filenames ([`5f034b5`](https://github.com/mcbeet/lectern/commit/5f034b59db0cf64fe056650983ae36efeae98f24))
* Lanternmc.com now returns a 403 ([`faaa2d3`](https://github.com/mcbeet/lectern/commit/faaa2d3b26bb1b20b3ae6ad73255edb6e11b0840))

### Documentation
* Document lectern scripts ([`fea9bbf`](https://github.com/mcbeet/lectern/commit/fea9bbf7682cd756022869eccdccd67a67e532d5))
* Document --prefetch-urls ([`4b4eaae`](https://github.com/mcbeet/lectern/commit/4b4eaae89fcd118eab2a3ff9a81cd3f340b4f61b))

## v0.6.1 (2021-03-03)
### Fix
* Make pyright happy ([`f15700c`](https://github.com/mcbeet/lectern/commit/f15700c1c5a5348248ac9947a167fe3931d74c31))

## v0.6.0 (2021-02-27)
### Feature
* Add merge modifier ([`907b630`](https://github.com/mcbeet/lectern/commit/907b630a23bf3f4d88c7a343c529a6a6e2fce07b))
* Add append modifier ([`d4e8be4`](https://github.com/mcbeet/lectern/commit/d4e8be4fb54da6c75b959ce569974b612aedde1a))
* Add base64 modifier ([`acd9d77`](https://github.com/mcbeet/lectern/commit/acd9d7740df3d519b7a19d59f1b98af0d0092d76))

### Fix
* Don't set any cache timeout ([`ebbb5a6`](https://github.com/mcbeet/lectern/commit/ebbb5a6710c8e63fdfe73d9dc7b07848c4ca6818))
* Report unexpected arguments for skip directive ([`f7ff720`](https://github.com/mcbeet/lectern/commit/f7ff720b7444135d888154940f7ed226e0a9dfdb))
* Add item_modifier directive ([`5e034d5`](https://github.com/mcbeet/lectern/commit/5e034d57f36a1f8719e88cd653e7fab8ffbfb5c2))
* Don't cache data url ([`c7517a8`](https://github.com/mcbeet/lectern/commit/c7517a844a3c09da9a448f8742c69f30b9478cc2))

### Documentation
* Udpate readme ([`a110a82`](https://github.com/mcbeet/lectern/commit/a110a823f333f277deff7137f32b133eb2d16ce5))

## v0.5.0 (2021-02-25)
### Feature
* Serialize images ([`7cf6fd9`](https://github.com/mcbeet/lectern/commit/7cf6fd944533a4ea9210f1f795bc4839c1a793de))
* Extract image fragments ([`1c6b71b`](https://github.com/mcbeet/lectern/commit/1c6b71bd0008163226394d77b8909f7459584732))

### Fix
* Use match_tokens() to check for a single code_inline ([`7117521`](https://github.com/mcbeet/lectern/commit/7117521388f5b76e0085d19301d1a9d5d5b7d86f))

## v0.4.0 (2021-02-25)
### Feature
* Add link fragments ([`b0d26d5`](https://github.com/mcbeet/lectern/commit/b0d26d530bd5029ea33bba8b1886a913af6ce125))

## v0.3.2 (2021-02-25)
### Fix
* Patch markdown_it to allow arbitrary data urls ([`bb5c05d`](https://github.com/mcbeet/lectern/commit/bb5c05df7d30e144d014fcaef36c84a802b7c51a))

## v0.3.1 (2021-02-24)
### Fix
* Markdown snapshots now use foldable sections ([`76359e0`](https://github.com/mcbeet/lectern/commit/76359e005ff0f833e0e3a134e78f15089a6dd3ba))

## v0.3.0 (2021-02-24)
### Feature
* Handle folded sections ([`9f611e5`](https://github.com/mcbeet/lectern/commit/9f611e57e766ba3e78bf7a15392fc4ab0e97650a))

## v0.2.2 (2021-02-22)
### Fix
* Resolve output_files relative to the context directory ([`73e4bcd`](https://github.com/mcbeet/lectern/commit/73e4bcdda5be64f5296641a9e66a048aaf35f1d5))

### Documentation
* Add command-line utility help text ([`e615ba1`](https://github.com/mcbeet/lectern/commit/e615ba13b61fc0c1625c538d8290b142d16e3ea3))

## v0.2.1 (2021-02-22)
### Fix
* Handle strip_final_newline in the fragment itself ([`d031607`](https://github.com/mcbeet/lectern/commit/d03160756140dc8fe6406a57869b39780c7f7846))

## v0.2.0 (2021-02-22)
### Feature
* Extract and serialize markdown ([`7827d61`](https://github.com/mcbeet/lectern/commit/7827d61a9fa298da55e05246c294c2a011750017))
* Implement strip_final_newline modifier ([`9aef7d4`](https://github.com/mcbeet/lectern/commit/9aef7d45d0db7b4f7bac667e351b09097e68c2d0))
* Add snapshot testing ([`316e806`](https://github.com/mcbeet/lectern/commit/316e8065a59571722cb0a4bdf2fd38912c818111))
* Add load method ([`81953af`](https://github.com/mcbeet/lectern/commit/81953af678e6e20237cbc7d689775c144ef51f16))

### Fix
* Allow empty modifier ([`c9937b9`](https://github.com/mcbeet/lectern/commit/c9937b96e7b9884027f61dfba719d22692a49d67))
* Don't drop modifier ([`8304433`](https://github.com/mcbeet/lectern/commit/8304433b592b7dd09ca914fd63084fca8cdbecd4))
* Add newline between loot table and advancement in README ([`7337a70`](https://github.com/mcbeet/lectern/commit/7337a70019cd86fa61c33bb212046111419173e8))
* Rename operators to modifiers ([`3886ec3`](https://github.com/mcbeet/lectern/commit/3886ec317b66a50ee0935dec5cb1f72eb3582ccc))

## v0.1.0 (2021-02-22)
### Feature
* Plain text extraction and serialization ([`49e8996`](https://github.com/mcbeet/lectern/commit/49e8996d3398a8683ea91de3df062e47707574c8))

### Fix
* Change document methods and add tests ([`8879b90`](https://github.com/mcbeet/lectern/commit/8879b909c00fa5299793ce90db8c1ee81d2af085))
