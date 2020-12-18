# Django 入門 
[参考リンク](https://docs.djangoproject.com/ja/3.1/intro/tutorial01/)
___

## 特徴
- Laravel, Rails とは異なり，MVT architecture を採用
- Flask よりリッチなコンテンツが簡単に作成可能

## ポイント
- メインのプロジェクトのルートディレクトリから再度 上記コマンドでアプリを作成することで，プロジェクトに様々な機能(アプリ)を付与していく
- アプリには独自の view(コントローラ) があるため，URL を簡単にプラグ & プレイすることができる
- **ビューを作成(追加)する場合**，以下の2ステップ
    - `views.py` に関数を追加
    - `urls.py` の `urlpatterns` に path を追加

## チュートリアル
- プロジェクトの作成 ([参考リンク](https://docs.djangoproject.com/ja/3.1/intro/tutorial01/)その１)
    - 仮想環境の作成
        - 仮想環境で作成するので，まず，`python -m venv [venvname]`
        - そんで，`. venv/bin/activate` で仮想環境をアクティベートする
            - ちなみに，オプション`-m`は，モジュール実行の意味．`-m`を外してコマンド叩くと，`No such file or directory` のエラー
    - django セットアップ
        - pip で django をインストールする
        - `django-admin startproject [mysite]` で，アプリのセットアップ
            - これで，ルートディレクトリに `[mysite]` ディレクトリが作成される
    - 一旦起動してみる
        - `python manage.py runserver` で開発サーバ起動，デフォルトのポートは 8000
            - ポート番号を変更したい場合は，コマンドライン引数で指定可能
        - migration エラー(alert) が出るが，今は ok
            - おそらくこの段階で，`db.sqlite3` が生成される
    - アプリケーションを作る(ここでいうアプリケーションは，サイトの一機能のことを指す)
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
        - 次は，URL に さっき作成した index 関数を対応づける必要がある．`polls` ディレクトリに，以下のような `urls.py` を作成する
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
- DB の設定([参考リンクその２](https://docs.djangoproject.com/ja/3.1/intro/tutorial02/))
    - DB の設定
        - mysite/setting.py では，DBタイムゾーン設定やミドルウェア設定など色々設定できる
    - モデル作成 **(MTV の M は MVC と同じ Model の意味!)**
        - polls/models.py で，モデル作成してみる
            ```python
            from django.db import models

            # Create your models here.

            class Question(models.Model):
                question_text = models.CharField(max_length=200)
                pub_date = models.DateTimeField('date published')

            class Choice(models.Model):
                question = models.ForeignKey(Question, on_delete=models.CASCADE)
                choice_text = models.CharField(max_length=200)
                votes = models.IntegerField(default=0)
            ```
        - 各クラスは，`models.Model` のサブクラス(継承クラス)で，クラス変数(プロパティ)には，DB フィールドを表現している
        - 型とか外部キーとかもつけれるよ
    - モデルの有効化
        - polls アプリを作成したことをプロジェクトに伝える必要がある
        - `mysite/settings.py` を
            ```python
            INSTALLED_APPS = [
                'polls.apps.PollsConfig',
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
            ]
            ```
            のように変更する．デフォルトで admin や auth などインストールされているが，不必要であればコメントアウトしても ok
    - migration に関しては割愛 (**理解して追記する**)
        - DB の変更を記録するもの(イメージ)
    - Django admin
        - コンテンツ管理のための管理サイト作成を行う
        - `python manage.py createsuperuser` で管理ユーザ作成
            - ユーザ名, メールアドレス, パスワードを求められるので入力
                - これって ユーザ名は `admin` のほうがいいの？
        - サーバー起動して，`/admin` にアクセスすると管理画面へのログイン画面が表示される
        - 管理画面では，プロジェクト内のアプリの編集や，管理ユーザの一覧表示，編集など色々行うことができる．(この辺は逐一調べて行ったほうがよさそう)
            - 作成したアプリはデフォルトでは管理画面に表示されなくて，表示したいアプリの `admin.py` に,
                ```python
                # polls アプリの場合
                from .models import Question
                admin.site.register(Question)
                ```
                と追加する必要がある．追加すると，アプリ内のデータを CRUD できる
- 公開用のインタフェース，ビューの作成([参考リンクその3](https://docs.djangoproject.com/ja/3.1/intro/tutorial03/))
    - ビューを作成する
        - polls アプリにビューを作成する
            - 今回は，投票結果と，投票画面，詳細を表示させる画面を実装したいので，`polls/views.py` に以下を追加する
                ```python
                def detail(request, question_id):
                    return HttpResponse("You're looking at question %s." % question_id)

                def results(request, question_id):
                    response = "You're looking at the results of question %s."
                    return HttpResponse(response % question_id)

                def vote(request, question_id):
                    return HttpResponse("You're voting on question %s." % question_id)
                ```
            - view に関数を追加したら，ルーティング設定が必要なので，`polls/urls.py` の `urlpatterns` に上記の関数を追加する
                ```python
                urlpatterns = [
                    path('', views.index, name='index'),
                    path("<int:question_id>/", views.detail, name="detail"),
                    path('<int:question_id>/results/', views.results, name='results'),
                    path('<int:question_id>/vote/', views.vote, name='vote'),
                ]
                ```
                今回は url に引数をとりたいので，上のように `<type: name>` で記述する
    - 使えそうなビューを作成する
        - `polls/views.py` に以下を追加する
            ```python
            from .models import Question

            def index(request):
                latest_question_list = Question.objects.order_by('-pub_date')[:5]
                output = ', '.join([q.question_text for q in latest_question_list])
                return HttpResponse(output)
            ```
            やってることは，
            - modelから Question を読み込み
            - Quesion から，`oder_by` メソッドで最新の投稿５件を取得する
            - カンマ区切りで `HttpResponse()` する
        - **しかし，このコードは見栄えがよくない．** データをどのように表示させるかは，**View** の役割ではなく，**Template** の役割なので，**View**で表示方法まで記述するのは好ましくない
            - こういう，本来外部プログラムに書くことをそのまま一緒に書いちゃうことを**ハードコーディング**という
        - `polls/templates/polls` を作成し，(なぜ二回 polls フォルダを作るのかは謎) `index.html` を作成する
        - `views.py` の `index()` に以下を追加する
            ```python
            from django.template import loader

            def index(request):
                latest_question_list = Question.objects.order_by('-pub_date')[:5]
                template = loader.get_template('polls/index.html')
                context = {
                    'latest_question_list': latest_question_list,
                }
                return HttpResponse(template.render(context, request))
            ```
            なんか，基本的に覚えた方がはやそうな雰囲気
    - 404 エラー処理を追加する
        - 今，存在しない `question_id` にアクセスしてもそのページが表示されるので，存在しない場合は 404 を返したい
            ```python
            from django.http import Http404
            from django.shortcuts import render

            from .models import Question
            # ...
            def detail(request, question_id):
                try:
                    question = Question.objects.get(pk=question_id)
                except Question.DoesNotExist:
                    raise Http404("Question does not exist")
                return render(request, 'polls/detail.html', {'question': question})
            ```
            基本的な try-except 構文．それとさっきの render を使ってるくらい．
    - ショートカットについて
        - Django にはよく実装される処理(上の html を rendering するとか，404 レスポンス返すとか...)のショートカットが存在する
            - あくまでショートカットなので，上で理解して，あとでショートカットに書き換えるくらいの気持ちで良さそう
        - render のショートカット
            ```python
            from django.shortcuts import render

            from .models import Question


            def index(request):
                latest_question_list = Question.objects.order_by('-pub_date')[:5]
                context = {'latest_question_list': latest_question_list}
                return render(request, 'polls/index.html', context)
            ```
            みたいにする．
            具体的には，ローダーをインスタンス化する手間が省かれる．
        - 404 レスポンスのショートカット
            ```python
            from django.shortcuts import get_object_or_404

            from .models import Question
            # ...
            def detail(request, question_id):
                question = get_object_or_404(Question, pk=question_id)
                return render(request, 'polls/detail.html', {'question': question})
            ```
            これは便利そう．
            try-except のほうが理解はしやすいけど，コード量はかなり減る．
    - テンプレートシステムを使う
        - 404 レスポンスのショートカットで，変数　`question` にはオブジェクトが入っている
        - 表示先の `detail.html` で，
            ```html
            <h1>{{ question.question_text }}</h1>
            <ul>
            {% for choice in question.choice_set.all %}
                <li>{{ choice.choice_text }}</li>
            {% endfor %}
            </ul>
            ```
            とすることで，html 内で，オブジェクトのメンバ変数など呼び出せる (これは Flask のテンプレートシステムと同じに思える．)
    - ハードコードされた URL を削除
        - `index.html` で，
            ```html
            <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
            ```
            こんな感じで，href の部分をハードコーディングしていると，`polls`を`specifics`とかに変えたいとなった場合，**`url.py`と`該当のhtmlファイル`の両方を書き換える必要がある．**
            ```html
            <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
            ```
            Django では，上のように href を `url.py` で定義した，**URL定義を引用することができる**
        - そうすることで，URLを変更したいとなった場合，`url.py`の変更のみで済む
    - URL 名の名前空間
        - Django プロジェクトに同名の URL 名がある場合 (例えば，polls の detail と，specifics の detail 両方実装する必要がある時など) は，**名前空間を定義することで解決できる**
        - `polls/url.py` に，
            ```python
            app_name = 'polls'
            ```
            を追加し，該当する html ファイルで，
            ```html
            <a href="{% url 'detail' question.id %}">
            ```
            こんな感じになってるやつを，
            ```html
            <a href="{% url 'polls:detail' question.id %}">
            ```
            こうすることで，`pollsのdetailか〜`と，プロジェクトが認識してくれる．
- フォームの作成 ([参考リンクその4](https://docs.djangoproject.com/ja/3.1/intro/tutorial04/))
    - こんな感じでつくる
        ```html
        <h1>{{ question.question_text }}</h1>

        {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

        <form action="{% url 'polls:vote' question.id %}" method="post">
        {% csrf_token %}
        {% for choice in question.choice_set.all %}
            <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
            <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
        {% endfor %}
        <input type="submit" value="Vote">
        </form>
        ```
        シンプルに radio で選択した項目を post する form．
    - `forloop.counter` は，そのまま何回ループしたかのカウンタ
    - データ改ざんの恐れがある form 送信では， csrf の可能性があるため，
        ```
        {% csrf_token %}
        ```
        で対策する．(laravel でもこんなんあった)
    - post された後に表示させる vote 関数を，
        ```python
        def vote(request, question_id):
            question = get_object_or_404(Question, pk=question_id)
            try:
                selected_choice = question.choice_set.get(pk=request.POST['choice'])
            except (KeyError, Choice.DoesNotExist):
                # Redisplay the question voting form.
                return render(request, 'polls/detail.html', {
                    'question': question,
                    'error_message': "You didn't select a choice.",
                })
            else:
                selected_choice.votes += 1
                selected_choice.save()
                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
                return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        ```
        こんな感じにする．(`HttpResponseRedirect`をインポートするのを忘れずに！)
        - ここで，**注目すべき**なのは，
            - `request.POST['choice']` で post されたデータを読み取っている点(空すなわち choice キーが未定義の場合は，KeyError が帰る)
            - `detail.html` に detail 関数では引数に取っていない `error_message` を引数に取っている点
            - カウンタが更新された場合，`HttpResponse` ではなく，`HttpResponseRedirect` を使用している点
                - これは Django 特有ではなく，一般的にそうするらしい．~~なんでかはシラン~~
        - 最後に result にアクセスしているので，result 関数を，
            ```python
            def results(request, question_id):
                question = get_object_or_404(Question, pk=question_id)
                return render(request, 'polls/results.html', {'question': question})
            ```
            こんな感じにする．で，テンプレートも作成
            ```html
            <h1>{{ question.question_text }}</h1>

            <ul>
            {% for choice in question.choice_set.all %}
                <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
            {% endfor %}
            </ul>

            <a href="{% url 'polls:detail' question.id %}">Vote again?</a>
            ```
    - 汎用テンプレートの使い方
        - URL から受け取ったパラメータを元に，DB からデータを取得し，テンプレートに表示させる．みたいなのは基本的によくあること．
        - Django では，これにもショートカットが提供されている
            - まず，`polls/urls.py` の URL からパラメータを受け取る部分(この場合は`<question_id>`)を`<pk>`に変更する．(pk は primary key の略)
                - *pk にするのは\"**そういうもん**\"らしい*
                ```python
                from django.urls import path

                from . import views

                app_name = 'polls'
                urlpatterns = [
                    path('', views.IndexView.as_view(), name='index'),
                    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
                    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
                    path('<int:question_id>/vote/', views.vote, name='vote'),
                ]
                ```
                こんな感じ．
            - で，view 関数やら detail 関数やら，
                データ取得→表示
                みたいな流れになってる関数を
                ```python
                class IndexView(generic.ListView):
                    template_name = 'polls/index.html'
                    context_object_name = 'latest_question_list'

                    def get_queryset(self):
                        """Return the last five published questions."""
                        return Question.objects.order_by('-pub_date')[:5]


                class DetailView(generic.DetailView):
                    model = Question
                    template_name = 'polls/detail.html'


                class ResultsView(generic.DetailView):
                    model = Question
                    template_name = 'polls/results.html'
                ```
                のように class で書く．
                **で，終わり．**
        - 汎用テンプレートは，これ以外にも色々あるらしい(やりながら調べる)
        - モデル名から，**引数を予想してくれてる??(ここが不明)**ことで，コード量が激減する
- 自動テスト ([参考リンクその5](https://docs.djangoproject.com/ja/3.1/intro/tutorial05/))

## Tips
- DB 接続 (SQLite の場合)
    - ターミナルで，`sqlite3 [db名]`
        - 今の場合は，`sqlite3 db.sqlite3`
    - コマンドは，MySQL と結構違う．(詳しくはggって)
        - `show databases;` は `.ta`
        - あとは普通に SQL (`select * from polls_choice` みたいな)
            
## 用語
- パーマリンク
    - パーマネントリンク(Permanent Link) の略
    - web サイトに個別に割り当てられているリンクのこと

## 参考リンク
- [Djangoドキュメント](https://docs.djangoproject.com/ja/3.1/intro/tutorial01/)