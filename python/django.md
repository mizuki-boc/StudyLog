# Django 入門

## 特徴
- Laravel, Rails とは異なり，MVT architecture を採用
- Flask よりリッチなコンテンツが簡単に作成可能

## ポイント
- メインのプロジェクトのルートディレクトリから再度 上記コマンドでアプリを作成することで，プロジェクトに様々な機能(アプリ)を付与していく
- アプリには独自の view(コントローラ) があるため，URL を簡単にプラグ & プレイすることができる

## チュートリアル
- プロジェクトの作成
    - 仮想環境の作成
        - 仮想環境で作成するので，まず，`python -m venv [venvname]`
        - そんで，`. venv/bin/activate` で仮想環境をアクティベートする
    - django セットアップ
        - pip で django をインストールする
        - `django-admin startproject [mysite]` で，アプリのセットアップ
            - これで，ルートディレクトリに `[mysite]` ディレクトリが作成される
    - 一旦起動してみる
        - `python manage.py runserver` で開発サーバ起動，デフォルトのポートは 8000
            - ポート番号を変更したい場合は，コマンドライン引数で指定可能
        - migration エラー(alert) が出るが，今は ok
            - おそらくこの段階で，`db.sqlite3` が生成される
    - アプリケーションを作る(ここでいうアプリは，サイトの一機能のことを指す)
        - `python manage.py startapp [polls]` で，polls というアプリを作る．
        - ここで `polls` ディレクトリが作成される
    - ビュー作成 (Django の view は MVC の C であることに注意！)
        - `polls/view.py` に移動，
            ```python
            from django.http import HttpResponse

            def index(request):
                return HttpResponse("Hello, world. You're at the polls index.")
            ```
        のように変更
        - 次は，URL に対応づける必要がある．`polls` ディレクトリに，以下のような `urls.py` を作成する
            ```python
            from django.urls import path

            from . import views

            urlpatterns = [
                path('', views.index, name='index'),
            ]
            ```
        - 次は，ルート(`mysite/urls.py`)の `urls.py` に，`polls` の view(コントローラ) を渡す必要がある
            - アプリごとに小さいコントローラが存在するイメージ．
            - 小さいコントローラをまとめるのが，`mysite/urls.py` となる (これが Django の良いところ！)
        - ルートの `urls.py` を以下のように変更する
            ```python
            from django.contrib import admin
            from django.urls import include, path

            urlpatterns = [
                path('polls/', include('polls.urls')),
                path('admin/', admin.site.urls),
            ]
            ```


## 参考リンク
- [Djangoドキュメント](https://docs.djangoproject.com/ja/3.1/intro/tutorial01/)