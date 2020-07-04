## Python 勉強ログ
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
