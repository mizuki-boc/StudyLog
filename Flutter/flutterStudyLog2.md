## Flutter 勉強ログ Part2
- [Issues](#issues)
    - 現状の問題点。解決したいイシューなど。
- [Loadmap](#loadmap)
    - 今後の方針。この StudyLog の終了地点を示す。
- [App](#app)
    - 作るアプリの構想
- [StudyLog](#studylog)
    - 日別に学んだことを書く。
---
## Issues
- android Studio から flutter プロジェクトを作成するとき、SDK のパスが通ってないと怒られる。毎回 C: の flutter ファイルを指定するのも面倒なので、どうにかしたい。
    - Android Studio の Setting に SDK パスを設定するところがあったので、そこに入力するといけるかも？
- アプリのサイズ感を確かめるために Android のエミュレータを起動させたかったが、何故か立ち上げることができなかった。多分原因は BIOS で仮想化を許可していないからな気がするが、どうにかしたい。
- mac で iOS デバッグもしたい。mac で android studio インストールする。
    - ファイル共有する方法も把握しておく。
- VScode と android studio の比較

    ||VSCode|Android|
    | --- | --- | --- |
    | フォーマット |  `Alt + shift + F` <br> いい感じ |  save or `ctrl + Alt + Enter` <br>たまにごちゃつく  |
    |ホットリロード|`r`<br>Start debugging から save |save <br> ⚡ <br> `r`|
    | メソッドの参照 | 右クリックからできる|  `Alt + Click`  |
    |リファクタリング|右クリックからできる|右クリックからできる|
    |ウィジェットのラップ|Refactor で Wrap できる|`Alt` + `Enter`|

## Loadmap
1. ✔ FireBase 環境構築
2. ✔ FireBase を用いたデモアプリの作成
    - ジムに行った日や滞在時間、体重の推移などストアするアプリ作ったら面白そう。
        - いちいちボタンを押してジムの入退室を管理するんじゃなくて、位置情報で入退室管理できたら面白そう。
3. Flutter のゲームフレームワークをチラ見する
4. アプリ王選手権にエントリするゲームの内容決める
5. 締め切り 12/13 までにリリース

## App
- メイン画面
    - 開始(入室)ボタンと終了(退室)ボタン


## StudyLog
## 8/18
- リリース(完成)に向けて意識したいこと。
    - **MVP (Minimum Viable Product) 開発** を意識する。
        - 余計な実装は後回しにしてコア機能 (アプリのフレーム) を重点的に実装。
- ジム(エニタイム)の入退室管理のアプリを作成する
    - **コア機能**
        - 時間記録 (Create)
            - エニタイムに入室したときに、ボタンを押すと、時間が記録される。
            - 退出するときに再度押すと、滞在時間が計算される。
        - 一覧 (Read, Update, Delete)
            - 過去の記録を一覧表示する
            - 記録の削除、編集
    - 応用機能
        - ボタンをいちいち押すのでなく、位置情報で記録。
        - 過去の記録をカレンダーで色付け表示する。
        - トレーニング内容の記録

## 8/20
- Dart はクラスをインスタンス化して呼び出す必要はないらしい
- VScode で保存したタイミングでホットリロードする場合、command で `flutter run` するのでなく、 Run タブの Start debugging からアプリを起動させると保存でホットリロードになる。 
- とりあえず公式 DOC みてどんな感じのデザインにするか決める
- [Place a floating app bar above a list](https://flutter.dev/docs/cookbook/lists/floating-app-bar) をみて実装してみた。かっこいいけどヘッダーに載せる情報もないので、今回はもっとシンプルな奴にする。

## 8/22
- firebase 環境構築 (Android) 
    - firebase (web) からプロジェクト作成、`google-serveces.json` を android/app 配下にコピー
    - 二か所の `build.gradle` にコードを追加する。
    - `Android Studio` の `pub get` は VScode ではターミナルで `flutter packages pub get`
    - location は `Asia northeast 2` が大阪。１は東京