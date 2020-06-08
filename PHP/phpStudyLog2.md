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