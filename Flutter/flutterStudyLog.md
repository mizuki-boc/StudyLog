## Flutter 勉強ログ Part1
- [Issues](#issues)
    - 現状の問題点。解決したいイシューなど。
- [Loadmap](#loadmap)
    - 今後の方針。この StudyLog の終了地点を示す。
- [Widget](#widget)
    - 学んだ Widget を自分なりに理解
- [StudyLog](#studylog)
    - 日別に学んだことを書く。
---
## Issues
- android Studio から flutter プロジェクトを作成するとき、SDK のパスが通ってないと怒られる。毎回 C: の flutter ファイルを指定するのも面倒なので、どうにかしたい。
    - Android Studio の Setting に SDK パスを設定するところがあったので、そこに入力するといけるかも？
- アプリのサイズ感を確かめるために Android のエミュレータを起動させたかったが、何故か立ち上げることができなかった。多分原因は BIOS で仮想化を許可していないからな気がするが、どうにかしたい。
- mac で iOS デバッグもしたい。mac で android studio インストールする。
    - ファイル共有する方法も把握しておく。

## Loadmap
1. ✔ FireBase 環境構築
2. FireBase を用いたデモアプリの作成
    - ジムに行った日や滞在時間、体重の推移などストアするアプリ作ったら面白そう。
        - いちいちボタンを押してジムの入退室を管理するんじゃなくて、位置情報で入退室管理できたら面白そう。
3. Flutter のゲームフレームワークをチラ見する
4. アプリ王選手権にエントリするゲームの内容決める
5. 締め切り 12/13 までにリリース

## Widget
- `Scaffold`
    - 日本語で「足場」
    - ベースとなるウィジェットで、あんまり多用するものでもないかも
- `Container`
    - html とかの container と同じ感じ。ひとまとめにするもの
- `Column`
    - 縦並びに表示
- `Row`
    - 横並びに表示
- `Text`
    - その名の通りテキストを表示させるウィジェット
    - css みたいな雰囲気でスタイルを定義したりもできる
- `TextField`
    - 入力フォーム的な感じ。これも html の input 的な感じの奴に似てる。
- `RaisedButton`
    - Raised 以外にもいろいろな種類のボタンがある。Raised は影がついてて浮き出てるデザイン
- `AlertDialog`
    - dialog を表示させる。js の alert() に似てる
- `ListView`
    - `Column`と見た目はにてるが、`Column` 異なりスクロールできるようにしてくれる。`Column` で同じことをするとはみ出てると警告される。
    - サーバーからデータをもらって、リスト表示するときはこっち
    - `scrollDirection` で横スクロールにもできる
- `GridView`
    - グリッド(格子)表示させる。`ListView`と似てる。
- `Expanded`
    - >ExpandedというWidgetは、RowやColumnの子Widget間の隙間を目一杯埋めたいときに使います。
    - [【Flutter基礎】Expandedについて](https://qiita.com/nannany_tis/items/d4114f615e4d53964121) 
## StudyLog
## 8/8
- KBoy の Flutter 大学を見て環境構築 (前にやってた)
- [GoogleのFlutterドキュメント](https://codelabs.developers.google.com/codelabs/first-flutter-app-pt1/index.html?index=..%2F..index#0)を参考に進めた。
- `use an external package` で Package get をクリックみたいな利賀があるけど、それっぽいボタンが見つからなかった。
    - ターミナルで `flutter packages get` で同じ処理ができるっぽい。
- `4 use an external package` の　main.dart を書き換えるとこでドキュメント通りに変更するとエラー出る。
    - [githubにissuesあった](https://github.com/flutter/flutter/issues/33752) この通り変更で解決
- ⚡ボタンでホットリロード。これすごい気がする。
- 最後らへんがよくわからんかった。
- part1 終了。Dart が分かってない感がすごい。勉強する。

## 8/11
- [Codelabs](https://codelabs.developers.google.com/codelabs/first-flutter-app-pt2/#0) part2 のチュートリアルを進める
- [Flutter コマンド一覧](https://qiita.com/kurun_pan/items/f9251b1827ce9dca9e14) VScode と android studio のどっちが使いやすいか試してみる。Vscodeの場合、ビルドなどコマンドで行う必要があるため、その辺の使いやすさを対象に比較する。
- 一回ビルドして、デバイスにアプリが表示されると terminal が入力待ち状態になるので、その時に `r` を入力するとホットリロードされる。
    - 詳しいコマンドは terminal に載ってる。

## 8/13
- `flutter run` した後、デバイス側でアプリを落とすとコネクションロストする。
- チュートリアル終了した。結構あっさり目で、コードの意味はいまいちわかってない。
- **Dart の final と const の違いに関して**
    - final も const も値が後から変更できない型
    - **final は** プログラム開始時で一度初期化され、初期化以降は代入による変更はできない。しかし、**メモリ領域の内容が変更されることについての制約はない。**
    - **const は**コンパイル開始に先だって初期化されていて、プログラムの実行を通じて不変であることが保証されている。つまり、**メモリ領域の内容も変更可能であることを指す。**
    - [参考](https://qiita.com/uehaj/items/7c07f019e05a743d1022)
- [Dart 入門](https://qiita.com/teradonburi/items/913fb8c311b9f2bdb1dd) をちょろっと読んだ。
- [Flutterドキュメント日本語版](https://flutter.ctrnost.com/)

## 8/15
- flutter プロジェクトを作成するとき、`flutter create ProjectName` で新しいプロジェクトを作成できる
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
- **画像をアセットから表示させる場合**は、`pubspec.yaml`の最後の `flutter:` にアセットを表記しなければならない。[flutter.dev](https://api.flutter.dev/flutter/services/AssetBundle-class.html)を参照。
- KBOY の動画見てると AppBar のテキストがデフォルトで center になってた。Text に Alt + Enter で center ウィジェットでラップすれば解決するけど、なぜ違うのかわからんかった。
- まとめ
    - KBOY Flutter 大学　入門チュートリアル終了。~(頑張った。)~　メジャーなウィジェットの使い方、文字の装飾、ページ遷移を学んだ。
    - 次回も Flutter 大学の チュートリアルを進めていく。firebase 環境構築くらいはやりたい。

## 8/16
- **BlueStacks で Android App を起動する場合**、`build/app/outputs/apk/debug/app-debug.apk` を BlueStacks にドラッグドロップでインストールできる。
- 外部パッケージのインポート
    - pub.yaml の　dependences に　`provider: ^4.3.2` 的な感じでほしいパッケージを記入すると、Android Studio の右上に `Pub get` が出てくるのでクリック。
- [【Flutter実践】ProviderパターンでModelを作成する](https://www.youtube.com/watch?v=iN2IjSQR7Fs&t=11s) を参考に進めた。
    - 結構理解が難しかった。
        - ステートレスウィジェットは把握しないので、final で定義された変数は変更することはできない。
        - consumer 配下では model が参照できる。メソッドも実行できる
        - `notifyListeners`すると状態の変化を通知することができる。
        - 状態を供給するにはアプリ全体を Provider に渡す必要がある。
    - これは理解するより使えるようになって、結果的に理解してました的なところを目標にしたほうがよさそう。

## 8/17
- [【Flutter実践】Firebase環境構築と、Firestoreのデータを取得してアプリで表示](https://www.youtube.com/watch?v=IiEsyHiIwxc) に沿って進める。
- Firebase は　iOS と Android 別々に環境構築する必要がある。
    - Windows では　iOS はできないので、mac でそこの作業だけできないか確認する。
- iOS の Firebase 環境構築
    - windows では Xcode 開けないので無理っぽい。ちなみに [動画](https://www.youtube.com/watch?v=IiEsyHiIwxc) で open コマンドを使ってたが、powershell では　`Invoke-Item` で代用可能。
- Android の Firebase 環境構築
    - 基本 Firebase のホームページに沿って進める
    - パッケージ名に関して
        - shift 二回押しで ファイル名検索
        - manifest で src/main にあるやつを選ぶ
        - package="~~~" みたいなとこがあるから、Firebase の Android パッケージ名にコピペする
    - google-services.json を android/app 配下にコピーする。
    - android ディレクトリ配下の build.gradle に コピーするやつをコピーする。
        - android/app 配下にも build.gradle があるので注意
    - android/app 配下の build.gradle にも コピーするやつをコピーする。
    - pubspec.yaml で pub get する
- Android に firebase を登録するとき、
    `
    **Plugin project :firebase_core_web not found. Please update settings.gradle.**
    **Plugin project :cloud_firestore_web not found. Please update settings.gradle.**
    `
    みたいなエラーが出てきた。結果[【flutter】firebase登録時にsetting.gradeでのエラー](https://qiita.com/yukou29good0910/items/c84b04d9a3fe1de8e7c8) のまんま書き換えたら通った。
- 実機 or BlueStacks でテスト or デバッグする時、右上に Debug と表示される件に関して
    - MyApp の build に `debugShowCheckedModeBanner: false` と追加することで消える。
- FireStore のデータを model から読んでリスト表示。[【Flutter実践】ModelからFirestoreのデータを取得する（mapの使い方も)](https://www.youtube.com/watch?v=xeaiMqPeyQk)
- とりあえず、Firebase で CRUD 実装くらいまでは勉強続けたい。終わり次第アプリ考えて開発始める。
- `main.dart` の配置を変更した場合、 `flutter run` では動かなくなる。
    - この場合、`flutter run lib/path/main.dart` で通常通り動く。
    - [【Flutter実践】FirebaseのFirestoreに値を追加する（try catchの使い方も）](https://www.youtube.com/watch?v=3gySprP_kw4&t=121s)ではディレクトリ構造変えても特に何もしていないように見えたが、なぜ。
    - むしろ毎回パス打つのは面倒なので、できれば `main.dart`の配置は変えない方が良い気がする。
        - 実行できないよ。的なダイアログが表示される。そこで `　main.dart` のパスを指定できた。解決。
- 例外処理で、try構文 に関して、try の中で、ほかのメソッド内で例外処理を発生させることで catch に流すとこがしっくり来た。動画の21分ごろの説明。
    - しかもエラー文が変数に入ってるので catch の中で流用できる。超賢い。
- `async-await` に関して
    - よくわかってないけど、await 順番に実行する。の意味。
    - 同時に実行されると処理が打ち消しあってしまう場合ときに使う。
    - 追加する文章を入力して、前のページに戻るとき、リストを更新するコードとリストを表示するコードとかは同時に行われるとよくない。(更新する前に表示されると意味ないので)そういうときに便利。

## 8/18
- [【Flutter実践】FirebaseのFirestoreの値を更新(update)する](https://www.youtube.com/watch?v=W0oKfFgoKpM) を参考に進める。
- モデルのクラスを定義し、(動画の例では Book クラス) 型として使用する。引数に定義したモデルの変数を受け取る時、null でもよい場合は `{}` で囲む。
-  `async await` が抜けててエラー出た
    - CRUD 実装出来たら勉強する。`Future` とか Dart 特有の型に関しても勉強する。
- CRUD 実装終了。
    - 動画ではダイアログの表示がうまくいってなくて、結局わからんままだった。
        - 動画ではエラーとして吐かれてたのに対して、こっちはエラー的なのは見当たらなかった。(見落としてるだけ？)
    - Android Studio のコード整形がうまくいかないときがある。
        - 結構見づらくなるので、結局 VScode かなと思ってきた。
    - まだ Dart の基礎がわかってなさすぎるので、把握したい。
        - まんまり深くやっても遠回りな気がするので、上に書いたよくわからん内容から調べる。
        - 
    - VScode と android studio の比較

    ||VSCode|Android|
    | --- | --- | --- |
    | フォーマット |  `Alt + shift + F` <br> いい感じ |  save or `ctrl + Alt + Enter` <br>たまにごちゃつく  |
    |ホットリロード|`r`|save or ⚡ or `r`|
    | メソッドの参照 | 右クリックからできる|  `Alt + Click`  |
    |リファクタリング|右クリックからできる|右クリックからできる|

    - `async`, `await` に関して **(同期処理と非同期処理)**
        - >Flutterでコードを書いていて最初につまずくポイントが恐らく非同期(asyncronous)処理だと思います。funcA-> funcBと実行したい時になぜかfuncB -> funcAという風に 順番が逆に実行されてしまう。それはfuncAが非同期処理を行なっているからです。
        - ネットワークからデータを取り出す、DB内のデータを触る、など、処理に時間のかかる関数があったときに、ほかの関数(前作ったアプリでいうリストを表示させる関数など)は処理を待たずに実行してしまう。ここは同期処理(順番に実行)してほしいので、`async-await`を使う。
            - で、dart の場合は `await`を書く場合は、外側の関数に `async` をつける必要がある。
    - `Future`　に関して
        - 関数を非同期処理として定義するための型。
        