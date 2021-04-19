## IT 系 全般に関する知識
- プログラミング全般に共通する知識を書き溜めていく
- トピックはバラバラ．カテゴリが微妙なものや，気になった or 触れたものからストックする
___
## **Stateless**と**Statefull**に関して
- State は「状態」を意味する
- **Stateless** の特徴
    - 「状態」を記憶しない。
    - このユーザはさっきどういうリクエストを送ってきたかとか、ログインしてるかとかはまったく記憶しない。
    - メリット
        - サーバのリソースをすぐに開放できる。
    - デメリット
        - 送信するデータが多くなる
    - 代表例
        - HTTP
- **Statefull** の特徴
    - Stateless の逆の特徴。
    - セッションの状態によってリクエストするレスポンスが変わる
    - 代表例
        - FTP, SMTP
- まとめ
    - FTP, SMTP など「手続き」を踏まないといけない場合は Statefull である必要がある。
    - 一方、手続きが必要でなく、サーバーに負荷がかかることが予知される場合は Stateless であったほうがよい

## WebSocket に関して
- Websocket は HTTP ベースでクライアント・サーバーの相互通信を実現する技術．
- URL で，先頭の `http` とか `https` とか `ftp` は通信のプロトコルを表す．websocket の場合は `ws`
    - `wss` は over SSL/TLS の意味
- 実装する ブラックジャック アプリに関して
    - Webアプリの場合，クライアントはブラウザからアクセスするので，クライアント側の実装(フロントエンド)は js でやるしかない．
    - 逆にサーバーサイドはなんでもいいので，Python で行う．
    - port 枯渇? によって複数ブラウザからは見れないので，gunicorn とかでサーバー起動する．(これ解決になってるかわからない．)
- 参考
    - [今さら聞けないWebSocket](https://qiita.com/chihiro/items/9d280704c6eff8603389)
    - [フロントエンドとバックエンドのリアルタイム通信の選択肢を教えて下さい](https://qiita.com/suin/items/00dee8bac706a6d66862)

## web で利用されるリアルタイム通信に関して
- web で利用されるリアルタイム通信は主に以下の３つ 
    - AJAX ポーリング
        - ざっくり言うと，javascript と XML を使ってサーバと非同期通信を行い，ポーリング(サーバ側がクライアント側に順番に要求がないかい確認すること．擬似的な双方向通信が可能になる．)する
        - リアルタイム性を高めようとすると，サーバ側の負担が大きくなる．
    - websocket
        - サーバ側とクライアント側にソケットを用意し，双方向通信を可能にする技術．
        - 高いリアルタイム性が求められるときに使う(ゲームなど)．サーバの負荷は少ない．
    - server-sent events (SSE)
        - サーバがクライアントにデータをストリーミングする方法．
        - 早いが websocket ほどではない．
- 参考
    - [フロントエンドとバックエンドのリアルタイム通信の選択肢を教えて下さい](https://qiita.com/suin/items/00dee8bac706a6d66862)

## WebDAV に関して
- WebDAV とは
    - WebDAV は Web-based Distributed Authoring and Versioning の略で， HTTP の拡張形式．
    - 主な機能は，クライアントであるウェブブラウザからウェブサーバーに格納されているファイル・フォルダの参照・編集・コピー・削除などの操作を可能にすること
    - 似たプロトコルで，SCP や FTP などがあるが，これらとは異なり別途ネットワーク設定をいじる必要がなく，(ポートを解放したり) HTTP に使用するポートのみで良いので簡単．
    - 一方，HTTP はファイル転送に最適化されているものではないので，FTP や　SCP のが安定する(らしい．)
- まとめ
    - 複数人に資料を配布したい場合は WebDAV, 特定の PC に送信する場合は FTP. みたいな運用になりそう
    - ~~DropBox や GoogleDrive でよくないか??~~

## Linux と Unix の違いに関して
- それぞれの歴史
    - Unix
        - 現存する OS の中でも最古．
        - 開発された当時は OS という言葉自体も新しかった．
        - アメリカのベル研究所が開発．
        - リリース当初は無料で公開されてた．
            - その結果，人気が爆発．有料化の流れに
    - Linux
        - Unix のライセンス契約の流れを受け，フィンランドの天才大学生リナースが開発．
        - リナース(Linus) が作った　Unix ライクな OS．ということで Linux という名前になった．
        - 現在もオープンソースで改変も配布も自由．
- ざっくりした違い
    - Linux は Unix に比べ後発の OS．
    - もともと全く異なるが，中身はかなり似てる．

## WebRTC に関して
- WebRTC とは
    - Web Real Time Communication の略
    - HTML5 で新しく策定された API の規格で， P2P 通信でブラウザ間のリアルタイムコミュニケーションを実現する為の仕組み
- P2P 通信
    - プロトコルはリアルタイム性重視の UDP/IP
- P2P 通信に必要な情報
    1. Session Description Protocol (SDP)
        - 通信に必要な各ブラウザの情報を示す文字列
        - セッションの属性，メディアの形式，IPアドレス，ポート番号，通信帯域，など
        - 片方の PC がもう片方に SDP を Offer して，相方が Answer する Offer/Answerモデルで通信を行う．
    2. Interactive Connectivity Establishment (ICE)
        - 多くの場合，端末は LAN の中にいる為， NAT された private な IP アドレスしか持っていない
        - global IP アドレスと，通信可能なポート番号を知る必要がある．(privateIP と globalIP + port が一対一対応している！)
        - STUN (Session Traversal Utilities for NATs)
            - P2P 通信は，ネットワーク側から見てお互いの PC がどのような情報(IPとかポート)を持っているかお互いが知っている必要がある．
            - ネットワーク側にいる STUN サーバーは，お互いの PC がどんな情報を持っているか PC に伝える仕事をする．
            - STUN サーバーと通信することで，ネットワーク側から見た自分の情報を知ることができて，シグナリングサーバを介して相手に自分の情報を伝える．
            - お互いの IP + port を知っているので，P2P 通信が可能になる．
        - TURN (Traversal Using Relay around NAT)
            - ↑の時点で P2P 通信は実現されているが，FW が設置されている場合は，STUN では UDP ポートは動的に割り振られるので，FW に穴を開けまくってることになり，セキュリティ的に問題あり
            - または，何らかの理由で NAT を超えられない場合に TURN サーバが通信の橋渡しをする
                - この「何らかの理由」がややこしい．
                - 例としては，ipv4 網と ipv 6網間の P2P 接続を試みた際にできへんやんけ．となるらしい．
            - あと，これはもはや P2P では無い．
    - この必要な情報を交換することを**シグナリング**といい，**シグナリングサーバ**を用いて行う．
- 参考リンク
    - [壁を越えろ！WebRTCでNAT/Firewallを越えて通信しよう](https://html5experts.jp/mganeko/5554/) ←わかりやすかった
    - [WebRTCの基本とP2P通信が成立するまでを学ぶ](https://qiita.com/daitasu/items/ae21b16361eb9f65ed43)
    - [WebRTCとは](https://www.ois-yokohama.co.jp/redois/wp_redois/?page_id=124)
    - [WebRTCの裏側](https://gist.github.com/voluntas/975bfa230e513d146965)
    - [STUN/TURN サーバーとは？](https://callcenter-trend.com/2018/06/05/voip-webrtc-stun-turn-server01/)
    - [新型コロナの自宅待機中に、ビデオチャットしながらゲームで遊べるサービスを作った話](https://qiita.com/aitaro/items/8a97d320f5586c6e7bb6)

=======
## IPsec に関して
- Security Architecture for Internet Protocol の略
- 暗号化によってパケットの秘匿や改ざん検知を実現するプロトコル
    - VPN 構築を実現するためのプロトコル
    - 低レイヤでの暗号化なので，アプリは暗号化に関して気にしなくていい

