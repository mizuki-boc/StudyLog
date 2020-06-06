PHP 学習ログ その２
--- 
- 学習管理 App 「StudyManager」 を作成する．

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
    - とりあえずボタンつくった．[参考](https://saruwakakun.com/html-css/reference/buttons)
- 次回
    - そもそも右のバーにカテゴリ表示じゃなくて，ボタンのよこに選択タブおいとくみたいな感じでよくね．
    - 右は Analytics とか？