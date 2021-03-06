# PHP 学習ログ その２
___
- 学習管理 App 「StudyManager」 を作成する．
- 必要要件
    - 勉強時間計測機能，分析(統計情報の表示)
    - ユーザ関連(login, logout, ...)
    - DB 関連
- UI に関して
    - 時計をメニューバーのところに配置したほうがいいかも
    - デザイン関連は最後にまとめて実装する．

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
    - お疲れ様でした (result) 画面の実装．
        - index → study → result と移って， study → result は実行時間を post する．
    - プルダウンにするか一言メモにするか考える．

## 6/15
- result 画面の実装．
    - index から memo を study に post, study から result に memo を post．(ここ入力　するとこないけど form に なってる．もうちょい綺麗にしたい．)
- session を使用した開始時刻と終了時刻の記録．
    - 以下参考URL
    - [Laravelでセッションを使ってみる](https://qiita.com/reflet/items/5638ab18fd7cededed17)
    - [Laravel7 Sessionの使い方](https://mebee.info/2020/05/16/post-10651/)
- 次回
    - セッション情報から継続時間を計算する．
    - その情報を DB に保存．(ここしっかり理解したい．)

## 6/15 (2)
- 実行時間の計算．
    - ```strtotime()``` でタイムスタンプにして，```gmdate('H:i:s', xxx)``` で H:i:s 表記に変換．
- ふと思ったが，終了時刻をセッション記録する必要ある？

## 6/16
- DB の作成, [Macでmysqlを扱う方法](https://qiita.com/fuwamaki/items/194c2a82bd6865f26045)
- ```.env```の編集． DB 関連箇所

## 6/17 
- DB 基礎学習 [テーブル,カラム,レコードの違い](https://academy.gmocloud.com/know/20160425/2259)
- DB 作成．(前回 root でさくせいしてて，それでもいいけど， mizuki で作成した．)
    - ```create databases [db_name]``` で，```ERROR 1044 (42000): Access denied for user``` ってエラーでたけど， root ユーザーで ```grant create on *.* to mizuki@localhost``` で mizuki に create 権限を付与することで解決．[参考](https://www.dbonline.jp/mysql/user/index6.html)
    - migrate でも権限エラーが発生したので，mizuki@localhost に全ての権限を付与した．(権限の管理方法について学ぶ必要あり．)
- migrate で作成したテーブルを DBeaver で確認．[DBeaver使い方メモ](https://qiita.com/12345/items/48f6856e32fd618ea307)
    - DBeaver からデータベース作成できるっぽい．今度試してみたい．
- seeder 作成して，デフォルト値の埋め込み．(これページ上から作れる仕様にしたいから，いらない気もするが，一応やってみた．)
    - DBeaver でテストデータの生成を確認．
    - プロパティの右下に更新ボタンがあって，これ押さないと反映されない．
- ___study 画面から result に遷移する時，意味のない form を作って　post してるけど，これ普通に画面遷移だとダメなん？___
- ブラウザ上で保存ボタンを押して，押した時に学習時間を計算し，それを DB に保存， DBeaver で確認．
- ___DB 作成から seeder 実行までのフロー (MySQL の場合)___
    1. CLI から MySQL にログイン，create する．
    2. laravel プロジェクトの .env の使用する MySQL の port番号,username,password を記入．
    3. migration ファイルの作成，実行．(テーブルの定義)
    4. seeder ファイルの作成，(デフォルトデータの挿入)
- 次回
    - 保存した記録を一覧表示するページ
    - メイン画面から一覧画面への遷移

## 6/18
- histroy.blade.php の作成．
    - ```$folder->memo``` で memo の表示．
        - 表でストアしたデータを表示
- study ページで無駄に　post リクエスト送ってたのを get に変更．
    - 普通に a タグで ```href={{ route('name') }}``` 的な感じでおk．
- DB レコードの削除ボタンの実装．
    - リンクで引数 (id) を受け取って ```$folder = Folder::destroy($id);``` で削除．
    - js の confirm() で削除していいか確認画面を表示させた．
    - ```onclick="return confirm(~~)"``` だけでいいので，結構簡単に実装できた．
    - 削除後は一覧画面にリダイレクトしてるけど，一瞬 ```/{id}/delete``` にアクセスしてる感じになってるけどこれどうなん？？
- 次回
    - ページアクセス制限をつける
        - いきなり /result とかにアクセスされると困る．
        - これログイン機能実装しないと無理？？？その場合はログイン機能実装する．
    - **memo が not null なので，バリデーションが必須！** これも実装する．

## 6/19
- migration(テーブルの定義)を追加するとき，not null のレコードがある場合，```php artisan migrate:fresh```でテーブルをすべて削除し，マイグレーションを実行し直す．
- ```unsigned()```は符号なしで　0 から 18446744073709551615 の値をとる．
    - ```bigIncrements()```は unsigned の bigInt みたいな感じ．
- users table を作成 (migrate) してない気がするけど，もともと入ってる．
    - デフォルトで (id, username, email など) 定義されてるっぽい．
    - もとからある users テーブルの元からある id を作成した folders テーブルの user_id と紐づける．
- 前やったチュートリアルではシーダーを一個ずつ実行すると書いていたが，[Qiita](https://qiita.com/shosho/items/b69db263a494edfe3b21)にまとめて実行する方法が書いてた．
- larabel6 以降の認証機能の変更に関して．
    - 前回のチュートリアルと同様に，```php artisan ui vue --auth```で行けるかと思ったけど，プロジェクトごとに```composer require laravel/ui```する必要があり．[Qiita参考URL](https://qiita.com/daisu_yamazaki/items/a914a16ca1640334d7a5)
        - **これ先にやっとかないと HomeController やらなんやらが上書きされてしまうので注意！！**
- デフォルトログイン画面と，アプリの紐付け
    - デザインはデフォルトのまま
    - ログイン，新規登録，ログアウトの実装．
- 次回
    - 現在，ログインしててもしてなくても履歴を見れるので，履歴とユーザを紐づける．
    - ログインしていない場合の画面の実装．
    - チュートリアルでは js で route('logout) にリクエストを送っているが，form 作って submit か，js で submit か，どっちか決める．
    - layout.blade.php で結構チュートリアルからそのまま引っ張ってきてる部分があるので，ここは修正する．

## 6/20
- ユーザとフォルダのリレーション作成．
    - 1ユーザに対して多フォルダが存在する今回の場合，User モデルに function で folder を定義する
    - で，```return $this->hasmany('App\Folder')```を記述．
    - コントローラーから DB のデータを取得する時は，```Auth::user()->folder()->get()```で認証されたユーザに紐づくフォルダを取得する．
    - DB に保存する時の forder の user_id は ```Auth::id()```でok (超便利)
- 未ログイン時，```route('login')```にリダイレクトする機能の実装
    - コントローラのメソッドの冒頭に ```Auth::check()```で場合わけする方法もあるが，毎回書くのはダサい．
        - → **ミドルウェアに任せよう．の発想．**
        - ```Middleware/Authenticate``` の redirectTo メソッドで未ログインの場合は /login にリダイレクトする．**(ここちょっと合ってるか自信ない．)**
        - 逆に，ログイン時はログイン画面にアクセスされたくないので，```MiddleWare/RedirectIfAuthenticated```にリダイレクト先を書く．[公式ドキュメント](https://readouble.com/laravel/7.x/ja/authentication.html)
- 問題点
    - **未ログイン時は /result や /history などの get メソッドで観覧するページへのアクセスはブロックできたが， /study などの post メソッドのページは Laravel のエラーメッセージが表示してしまう問題．**
- 次回
    - デザイン関連
        - vue なり React なりを勉強する．
        - そもそもどういうものなのか理解できてないため，調べる．
    - 問題点の解決
        - エラーハンドリングにヒントがあるかも．(?)

## 6/21
- vue に入門することにした．[vue VS React](https://qiita.com/102Design/items/ae018dc80a4d879d92a8)
- laravel からは離れるので，jsStudyLog にまとめる．