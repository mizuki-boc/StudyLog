# Python 勉強ログ
python で遊びついでに知ったことをメモする
___

- pip install で SSL 関連のエラー
    - matplotlib をインストールしようとしたときに発生．
    - pyenv で python のバージョンアップすることで解決
        - その間に色々試してて， Xcode アプデしたりしてるからそれもあるかも．

## 7/4
- heroku に line-message-bot をデプロイしようとしたら，```ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.``` みたいなエラー発生．
    - builder のインストール， requirements.txt を最小限に留めたりいろいろ試したが，解決せず．
    - heroku は port 番号が毎回変わるらしい(?)ので，環境変数から使用されている port を取得して，```app.run(port="取得したport")```にしたら解決．
    - 他にも, pyroomacoustic のインストールエラーも発生してたが，いらないので requirements.txt から削除した．(log みたら pyroomscoustic のインストールのとこでひっかかってた)
- studyLog の git commit を自動化したい
    - コメントは日付とかでいいから，ワンクリックで git add. から push までやりたい
- **push するたびに　requirement.txt の内容全てインストールしてるように見えるが，これなんとかならない？**

## 7/5
- line-api に関して
    - 特定のメッセージがユーザから送られてきた時，オウム返し + 特定のメッセージ の２つ返信するコード書いてみたけど，エラー．
    - エラーメッセージよくわかんかた．たぶん一度に２通以上送れない．
        ```python
        # オウム返しする時
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="送信したメッセージ:"+event.message.text))
        ```
- ngrok に関して
    - heroku 上のプログラムからラズパイ上のプログラムを動かすのがむずい問題
        - solution 1 - ソケット通信
            - これ，同一ネットワーク上にないと厳しそう．
            - でも面白そうだから試してみたい
        - solution 2 - ラズパイでホストする
            - line api の web hook にのせる　url がない，
    - ngrok ... ローカル PC 上で稼働しているネットワークサービスを外部公開できるサービス
        - ラズパイでホスト (localhost: 8000 とか) して，ngrok で url 得る．
        - line api の webhook に url のせる．
        or
        - 研究室のマシンでホストする，ラズパイと同一ネットワークないなので，ソケット通信する
    - 起動方法
        - flask なり laravel なりのアプリをローカルで起動する．
        - ```ngrok http port番号``` で　url でてくる
- 実装に関して
    - 参考
        - [LINEでおうちの鍵を開け締めする](https://qiita.com/t-funaki/items/2a3bbed8f63d2dc660a3)