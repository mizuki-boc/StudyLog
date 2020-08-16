## Flutter 勉強ログ
- widget は別でまとめて、勉強ログは日別にまとめる。
---
## Issues
- android Studio から flutter プロジェクトを作成するとき、SDK のパスが通ってないと怒られる。毎回 C: の flutter ファイルを指定するのも面倒なので、どうにかしたい。
- アプリのサイズ感を確かめるために Android のエミュレータを起動させたかったが、何故か立ち上げることができなかった。多分原因は BIOS で仮想化を許可していないからな気がするが、どうにかしたい。
    - エミュレータはクソ遅いらしいので、実機買ったほうが早いかも。

## Loadmap
- FireBase 環境構築
- FireBase を用いたデモアプリの作成
- Flutter のゲームフレームワークをチラ見する
- アプリ王選手権にエントリするゲームの内容決める
- 締め切り 12/13 までにリリース

## 学んだ Widget
- ```Scaffold```
    - 日本語で「足場」
    - ベースとなるウィジェットで、あんまり多用するものでもないかも
- ```Container```
    - html とかの container と同じ感じ。ひとまとめにするもの
- ```Column```
    - 縦並びに表示
- ```Row```
    - 横並びに表示
- ```Text```
    - その名の通りテキストを表示させるウィジェット
    - css みたいな雰囲気でスタイルを定義したりもできる
- ```TextField```
    - 入力フォーム的な感じ。これも html の input 的な感じの奴に似てる。
- ```RaisedButton```
    - Raised 以外にもいろいろな種類のボタンがある。Raised は影がついてて浮き出てるデザイン
- ```AlertDialog```
    - dialog を表示させる。js の alert() に似てる
- ```ListView```
    - ```Column```と見た目はにてるが、```Column``` 異なりスクロールできるようにしてくれる。```Column``` で同じことをするとはみ出てると警告される。
    - サーバーからデータをもらって、リスト表示するときはこっち
    - ```scrollDirection``` で横スクロールにもできる
- ```GridView```
    - グリッド(格子)表示させる。```ListView```と似てる。
- ```Expanded```
    - >ExpandedというWidgetは、RowやColumnの子Widget間の隙間を目一杯埋めたいときに使います。
    - [【Flutter基礎】Expandedについて](https://qiita.com/nannany_tis/items/d4114f615e4d53964121) 

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

## 8/13
- ```flutter run``` した後、デバイス側でアプリを落とすとコネクションロストする。
- チュートリアル終了した。結構あっさり目で、コードの意味はいまいちわかってない。
- **Dart の final と const の違いに関して**
    - final も const も値が後から変更できない型
    - **final は** プログラム開始時で一度初期化され、初期化以降は代入による変更はできない。しかし、**メモリ領域の内容が変更されることについての制約はない。**
    - **const は**コンパイル開始に先だって初期化されていて、プログラムの実行を通じて不変であることが保証されている。つまり、**メモリ領域の内容も変更可能であることを指す。**
    - [参考](https://qiita.com/uehaj/items/7c07f019e05a743d1022)
- [Dart 入門](https://qiita.com/teradonburi/items/913fb8c311b9f2bdb1dd) をちょろっと読んだ。
- [Flutterドキュメント日本語版](https://flutter.ctrnost.com/)

## 8/15
- flutter プロジェクトを作成するとき、```flutter create ProjectName``` で新しいプロジェクトを作成できる
- [KBoy の Flutter 大学](https://www.youtube.com/channel/UCReuARgZI-BFjioA8KBpjsw)
    - android studio ではコマンドS (保存) するとホットリロードする機能もある
        - あまり VScode で開発する意味はない？かも
- 今回は android studio で開発してみる
    - ctrl + Alt + L でコード整形
    - なれの問題も当然あるけどやりにくい。
    - android studio がクッソ遅い気がする
- Alt + Enter でコードに関するショートカットが使える
    - ウィジェットでラップ、削除、パディングなど
- **ページ表示はスタック構造**になってる。遷移すると新しいページがスタックされ、戻るのはポップする。
- ctrl 押しながら遷移先のファイルのクラスをクリックで、そのクラスのファイルに飛ぶ。便利。
- android studio で保存するとホットリロードされるが、別ファイルの内容は各々保存する必要がありそう。
    - 多分、main.dart を保存したら解決したっぽい
- **画像をアセットから表示させる場合**は、```pubspec.yaml```の最後の ```flutter:``` にアセットを表記しなければならない。[flutter.dev](https://api.flutter.dev/flutter/services/AssetBundle-class.html)を参照。
- KBOY の動画見てると AppBar のテキストがデフォルトで center になってた。Text に Alt + Enter で center ウィジェットでラップすれば解決するけど、なぜ違うのかわからんかった。
- まとめ
    - KBOY Flutter 大学　入門チュートリアル終了。~(頑張った。)~　メジャーなウィジェットの使い方、文字の装飾、ページ遷移を学んだ。
    - 次回も Flutter 大学の チュートリアルを進めていく。firebase 環境構築くらいはやりたい。

## 8/16
- **BlueStacks で Android App を起動する場合**、```build/app/outputs/spk/debug/app-debug.apk``` を BlueStacks にドラッグドロップでインストールできる。
- 外部パッケージのインポート
    - pub.yaml の　dependences に　```provider: ^4.3.2``` 的な感じでほしいパッケージを記入すると、Android Studio の右上に ```Pub get``` が出てくるのでクリック。
- [【Flutter実践】ProviderパターンでModelを作成する](https://www.youtube.com/watch?v=iN2IjSQR7Fs&t=11s) を参考に進めた。
    - 結構理解が難しかった。
        - ステートレスウィジェットは把握しないので、final で定義された変数は変更することはできない。
        - consumer 配下では model が参照できる。メソッドも実行できる
        - ```notifyListeners```すると状態の変化を通知することができる。
        - 状態を供給するにはアプリ全体を Provider に渡す必要がある。
    - これは理解するより使えるようになって、結果的に理解してました的なところを目標にしたほうがよさそう。