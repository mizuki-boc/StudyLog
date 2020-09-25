## 目次
___
- [概要](#概要)
- [目標](#目標)
- [開発ログ](#開発ログ)
- [反省点](#反省点)

## 概要
___
- ストリーマーの配信を API (または webhook) から受け取って、受け取ったらユーザに通知するサーバ
- youtube, twitch, niconico くらいは対応させたい。
    - 上記以外の動画サイトにも対応できるような設計にしたい。
- ゴール
    - サーバーが配信を感知すると、ユーザーにメッセンジャー(Line, 今後作るアプリ)経由で通知する

## 目標
___
- スクレイピングの基本習得
    - youtube, twitch は API 使用。niconico は API ないのでスクレイピングで対応。
- 対応サイトのスケール (スケールできるような設計)
    - スケールしやすい構造。可読性を高める。
- 設計し、工数を定める。
    - 期限を設けて、それに従ってコーディング。git にコミットするタイミングも合わせる。
- 前回のプロジェクト(ブラックジャック)の反省点を活かす

## 設計
- python 仮想環境を構築する
    - なんか便利そうなのでこの際に勉強しとくことにする
- サーバー立てる
    - flask で実装。herokuでホスティング
    - フロント部分は必要ないかな
- メッセンジャー機能の実装 (最小機能)
    - フロントのボタン (トリガー) を押すと line で通知するようにする．みたいな実装してみる
- youtube, twitch API 触る
    - 基本的な動きを学ぶ
- 学んだ　API で放送時に通知する仕組みを実装する
- スクレイピングの基礎を勉強する
- niconico に対してスクレイピングして、放送中かどうかを判断できるようにする。(これが結構きつそう)
- 作った関数をサーバーに乗っける
- で、大体10日間くらいで終わりたい。。。。

## 開発ログ
### 9/18
- python 仮想環境を構築する
    - 実行手順
        - 目標のディレクトリで，`python -m venv [newenvname]` 実行．
            - newenvname はなんでもいいらしいが，venv にしとくのがオススメらしい
        - `. [newenvname]/bin/activate` で，仮想環境のアクティベートを行う
        - で完了．仮想環境に入ってる状態と入ってない状態で `pip freeze` とかが異なると思う
        - `deactivate` で終了
    - python のバージョンを変更する
        - 仮想環境上の python のバージョンは，ローカルのバージョンと同じになる．
        - バージョンを変更するには，
    - 参考 URL
        - [venv: Python 仮想環境管理](https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e)
        - [venvで作成した仮想環境内のPythonバージョンを変更したい](https://dev.classmethod.jp/articles/change-venv-python-version/)
- heroku にデプロイ
    - 前回(web-blackjack) の反省を踏まえ，まずデプロイしてみる
    - heroku は公開ポート番号が固定で指定できない．
    - ので，python では
        ```python
        port = int(os.environ.get("PORT", 5000))
        ```
        とかで，環境の公開ポート番号を取得する
- Line bot の作成
    - なんか Qiita とかで記事見ながらおうむ返しBOT 実装したのにかえってこやんやんけと思ったら，Line Developer で use webhook がオフになってただけだった．
    - ブロードキャストする
        - `line_bot_api.broadcast(TextSendMessage(text='友達全員にBroadcast'))`
        で可能
        - 今回は index ページにアクセスすることをトリガーにして，ブロードキャストした
            - 今後は配信を感知した時にブロードキャストするようにする
- 次回
    - youtube, twitch API を触ってみる
    - 参考になりそうなリンク集
        - [ニコニコをスクレイピングする](https://ameblo.jp/suzikisyou/entry-12573470259.html)

### 9/25
- youtube, twitch API を触ってみる
    - 共にあんまり記事がなく，難しい．(特に Twitch は Qiita にも記事がない)
    - Twitch は [公式DOC](https://twitchio.readthedocs.io/en/rewrite/twitchio.html) の，`Topics > class twitchio.webhook.StreamChanged(user_id)` の項目がそれっぽい．読む時間なかったので次回実験してみる
        - OAuth token エラーが出る．トークンは Twitch コンソールから取得できるのだが，どこに渡せば良いかわからない．
    - youtube api は，json は受け取れるものの，放送中かどうかを示すキーがどれなのかわからなかった．
- 次回
    - youtube, twitch API を触ってみる
    - 参考になりそうなリンク集
        - [ニコニコをスクレイピングする](https://ameblo.jp/suzikisyou/entry-12573470259.html)

## 反省点