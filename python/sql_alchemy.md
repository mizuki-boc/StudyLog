# SQLAlchemy の使い方 + heroku の PostgleSQL に対応し、デプロイ
- 目的
    - discord で Bot 作成、heroku にデプロイ済み。
        - heroku の PostgleSQL を python から扱えるようにしたいのでチュートリアル
        - ついでに flask も思い出す。
- 参考リンク
    - [FlaskとPostgreSQLでウェブアプリを作ってHerokuで無料で運用する](https://qiita.com/croquette0212/items/9b4dc5377e7d6f292671#%E6%A6%82%E8%A6%81)
- リポジトリ
    - [github](kokonirinnku)

## SQLite3
- SQLite3 とは
- やってみた
    - sqlite3 をインストールして、
        ```
        sqlite> .open --new C:/Users/mizuk/Desktop/project/db/test.db
        sqlite> create table test_teble (
        ...> testdata        integer);
        sqlite> .tables
        test_teble
        sqlite> begin transaction;
        sqlite> insert into test_table (testdata) values (1996);
        Error: no such table: test_table
        sqlite> insert into test_teble (testdata) values (1996);
        sqlite> commit;
        sqlite> select * from test_teble
        ...> ;
        1996
        ```
        まず、任意の場所に `.open --new ~~` で新たな DB を作成する
        次に、`create table ~~~` でテーブルを作成する
        引数に、カラムを定義する。今回は int 型の testdata を定義した
        `begin transaction`して、`insert into ~~~`で任意のテーブルのカラムにデータを入力する
        この時点で DB と同じディレクトリになんかよくわからんファイルができる。
        `commit` することで、よくわからんファイルが消えて、データが代入される。
        `sekect * from TABLE_NAME` で確認
- 次回
    - トップの参考リンクのレコードを表示してみるから
- 参考リンク
    - [SQLite 3.32.3 のインストール，データベース作成，テーブル定義（Windows 上）](https://www.kkaneko.jp/tools/sqlite3/sqlite3.html)