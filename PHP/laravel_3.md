## PHP 学習ログ その３
___
- F609 のエアコンコントローラを作成する．
- 方針
    - フレームワークは Larave
    - Line API でユーザからのメッセージを bot を通して取得．
    - F609 メンバ以外のリクエストには答えないように，ログイン機能の実装．
    - 不正なリクエストを監視する機能の実装．
    - ラズパイ連携．ラズパイ-Python-LineAPI, ラズパイ-Laravel-DB
- 懸念点
    - 研究室 PC でホストすることになると思うが，セキュリティ的には大丈夫？

## 6/29 
- 学んだこと
    - Line Message API に関して．
        - Line Massage API は Line 内でのメッセージを特定のサーバー (/callback) に post してくれる．(らしい)
        - なので，サーバーが必要．
    - heroku に関して
        - 月ごとに一定の無料利用枠が与えられ，超過すると停止するらしい．
        - 30 分以上アクセスがない時は，自動でシャットダウンしてくれる．
            - 次回起動時は少し時間がかかるらしい．(30分に一度リクエストを送り続けることで回避できるっぽい)
        - 今回想定している利用方法では十分っぽい．
- やること
    - heroku 環境構築(環境というか，heroku-cli 的なやつ)
        - ドメインも獲得(?)できるっぽい(??)
    - flask でコード書いて，heroku にデプロイ
- 参考      
    - [【LINE Messaging API】みんなの LINE へプログラムからメッセージを送りたい](https://qiita.com/yuu-eguci/items/1a572d83d3faf306ed08)
    - [【Heroku】無料プランの概要](https://www.shookuro.com/entry/2018/05/02/133225)
