PHP 学習ログ
---
- php での web アプリ開発の勉強記録．
- Markdown 記法の練習にもなれば．．．

## 5/27
- やったこと
    - php 環境構築
    - composer のインストール， laravel のインストール
    - composer create-project laravel/laravel "プロジェクト名"でフォルダ作成
- できなかったこと
    - https://qiita.com/yamato3310/items/fbef9f5cc450d69db156 を参考に作成したけど，localhostでアクセスできず．
- 明日の todo
    - ブックマークしてるphp入門できそうな気がするからやってみる．

## 5/28
- やったこと
    - https://www.hypertextcandy.com/laravel-tutorial-todo-app-list-folders
        - ↑に`http://todos/~~にアクセスすると~`みたいな感じで書いてるが，おそらく環境が違うため，できない．
        - ↑　`php artisan serve` すると可能
    - qiita みながら mysql インストール，DB 作成
    - migration で詰まったけど， .env の password が secred になってただけやった．設定したユーザ，パスで通った．
- できなかったこと
    - migration の考え方がわからなかった．(テーブルの定義ということ？)
    - テストデータの挿入．sequal pro で DB みようとしてもみれない．
- 明日の todo 
    - sequal pro のエラー解決，[php入門](https://www.hypertextcandy.com/laravel-tutorial-todo-app-list-folders) 続ける
    
## 5/29
- やったこと
    - > テストデータの挿入．sequal pro で DB みようとしてもみれない．
        - sequel pro は mysql 8.x に対応してないらしい．
            - DBeaver で同じことしたら，見れた．
    - > sequal pro のエラー解決 
        - table 名が間違ってた．db 再度作成， migration で解決．

## 5/30
- やったこと
    - tutorial の続き．
        - blade.php のファイルで参考演算子を用いて読み込む css 変えててすごかった．(チュートリアル (3) の最後らへん)
        - アクセサで css クラスも定義するのすごい便利．
    - > migration の考え方がわからなかった．(テーブルの定義ということ？)
        - [公式 DOC](https://readouble.com/laravel/5.7/ja/migrations.html)
- できなかったこと
    - 外部キー, migration がいまいちワカラン
    - SQL の基礎 where とかなんとか

## 5/31
- やったこと
    - クロスサイトリクエストフォージェリ対策について．
    - MVC モデルの理解．(理解できてる気がしてきた．)
        - データベース周りに関してはイマイチわかってない．
- 明日の todo
    - (5)入力値バリデーションから．