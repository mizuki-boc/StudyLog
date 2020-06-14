PHP 学習ログ その２
--- 
- 学習管理 App 「StudyManager」 を作成する．
- 必要要件
    - 勉強時間計測機能，分析(統計情報の表示)
    - ユーザ関連(login, logout, ...)
    - DB 関連

## 6/5
- プロジェクト作成
    - ```composer create-project --prefer-dist laravel/laravel SampleProject``` で新規プロジェクト作成
- 「StudyManager」の目的を決めた
    - 個人用の管理App
    - ログイン機能

## 6/6
- css 作成，読み込み
    - public/css/styles.css の構造にする，
    - asset() で public 以下のファイルパス読み込み．
        - ```<link rel="stylesheet" href="{{ asset('css/styles.css') }}">```
    - リセット css (今回は destyle.css )を使ってみた．
    - 前 (portfolio) css の class 名がごちゃごちゃになった反省があるので，今回はキレイにしたい．[class名に使えそうな英単語集](https://taneppa.net/class_name_english/)
- レスポンシブ対応に関して
    - html head に ```<meta name="viewport" content="width=device-width, initial-scale=1.0">``` 書かないとダメ
    - 細かい部分は全体のレイアウトが固まってきてからにする．
- メインコンテンツのデザインに関して
    - いまいち固まってない．
    - とりあえずボタンつくった．[デザイン参考](https://saruwakakun.com/html-css/reference/buttons)
- 次回
    - そもそも右のバーにカテゴリ表示じゃなくて，ボタンのよこに選択タブおいとくみたいな感じでよくね．
        - 右は Analytics とか？
    - ストップウォッチは js で実装して，html 上で更新される経過時刻を PHP で取得し，処理する方針でいく．
        - [PHPでHTMLの値を取得](https://teratail.com/questions/25144)

## 6/7
- 時計機能の実装
    - [jsコード参考](https://qiita.com/delph/items/9c702cdf03a5679d93e0)
- 時刻の受け渡しに関して
    - ~~onClick で js 起動，時間を取得して~~
    - ~~js で時計表示，スタートボタン押すと js 関数から post する~~
    - タグを読むのでなく，バックとフロントで切り分ける.(ユーザからは同一に見せるが，実際は異なるようにする.)(このほうが MVC モデルっぽい？？)
        - ___サーバーとクライアントでタイムゾーンが異なる時，差が生じるが，これはいったん無視することにする．(後で修正する)___
- 次回
    - [PHP で時刻を取得する](https://blog.codecamp.jp/php-datetime) を参考に作成．
    - running の get と post がごちゃってる．修正する．

## 6/8
- サーバー側時計機能の実装
- timezone 設定
    - config/app.php の 'timezone'=>'UTC' を 'Asia/Tokyo' に変更
- runningPage で経過時間を表示する
    - [jsのセミコロンに関して](https://qiita.com/igayamaguchi/items/ac48b7e12890351ee55a)
    - elapsed_time.js を作成．
    - 経過時刻も同時にサーバー側でも計算する？？？

## 6/9
- プルダウンの選択肢実装．
    - destyle.css で select とかのデザインも消えてる．
    - デザインは全体のバランスも考慮したいので，いったんこのままで最後に決める．
    - 暫定でサンプル値を入力しているが，最終的にはユーザが自由に選択肢を作成できるようにしたい．
        - のちに詳しく考える必要があるが，予めテンプレを用意し，その中から追加して選択するーみたいな感じでもいいかな？
- 次回
    - プルダウンで選択した項目を post して running page に表示させる．

## 6/13
- select で選択したカテゴリを post する方法がわからなかった．
- ルーティングに記述している get と post の違いを正しく理解できていない
- そもそもカテゴリを追加して，記録時に登録．という流れより，ひとことメモと一緒に実行できる方がよくないかな

## 6/14
- 入力した一言メモを遷移先の画面に post する機能の実装 
    - html の form の action で {{ route(~~~) }} みたいにしてたが，ここは flask とかでやってたシンプルにルート情報だけでいい．(この基本的なとこでめっちゃ詰まった．)
    - [Laravel7 フォームのリクエストデータを取得して表示する](https://mebee.info/2020/05/22/post-10635/)
    - laravel5 とかの情報は結構ヒットするけど，全く使えないと思ったほうが良い．
- github に関して
    - 本来，プロジェクトの設計に基づいてステップごとに commit するらしい．
- 次回
    - お疲れ様でした 画面の実装．
    - プルダウンにするか一言メモにするか考える．