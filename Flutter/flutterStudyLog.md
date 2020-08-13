## Flutter 勉強ログ
---
## 8/8
- KBoy の Flutter 大学を見て環境構築 (前にやってた)
- [GoogleのFlutterドキュメント](https://codelabs.developers.google.com/codelabs/first-flutter-app-pt1/index.html?index=..%2F..index#0)を参考に進めた。
- ```use an external package``` で Package get をクリックみたいな利賀があるけど、それっぽいボタンが見つからなかった。
    - ターミナルで ```flutter packages get``` で同じ処理ができるっぽい。
- ```4 use an external package``` の　main.dart を書き換えるとこでドキュメント通りに変更するとエラー出る。
    - [githubにissuesあった](https://github.com/flutter/flutter/issues/33752) この通り変更で解決
- ⚡ボタンでホットリロード。これすごい気がする。
- 最後らへんがよくわからんかった。
- part1 終了。Dart が分かってない感がすごい。勉強する。

## 8/11
- [Codelabs](https://codelabs.developers.google.com/codelabs/first-flutter-app-pt2/#0) part2 のチュートリアルを進める
- [Flutter コマンド一覧](https://qiita.com/kurun_pan/items/f9251b1827ce9dca9e14) VScode と android studio のどっちが使いやすいか試してみる。Vscodeの場合、ビルドなどコマンドで行う必要があるため、その辺の使いやすさを対象に比較する。
- 一回ビルドして、デバイスにアプリが表示されると terminal が入力待ち状態になるので、その時に ```r``` を入力するとホットリロードされる。
    - 詳しいコマンドは terminal に載ってる。