# セキュリティ全般の話

## VPN (Virtual Private Network)
- VPN とは
    - 仮想的なプライベートネットワークのことで，インターネット等の公衆網を利用する場合でも，IPsec で高度なセキュリティを実装できるので，安全に拠点間通信を実現できる
- VPN の種類
    - インターネットVPN
        - セキュリティプロトコルに IPsec を利用した IPsec-VPN と，SSL を利用した SSL-VPN がある．
    - IP-VPN
        - IP-VPN というと，MPLS-VPN のことで，経路情報の探索に MPLS を採用している
        ```
        MPLS（ Multi-Protocol Label Switching ）は、ラベルと呼ばれるタグを使用したパケット転送技術
        ```
- VPN 接続のタイプ
    - サイト間VPN
        - VPN を実装したルータ同士を接続する構成，企業の拠点間を接続する場合はこっち．
        - ルータが，パケットの暗号化を行ってくれるため，クライアントPCが暗号化する必要はなく，専用ソフトのインストールなどの必要もない
        - **IPsecを実装したルータやセキュリティ製品（ASAなど）はVPNゲートウェイと呼ばれる**
    - リモートアクセスVPN
        - VPN を実装したルータと，VPN クライアントソフトをインストールした PC とを接続する構成．

## IPsec
- IPsec とは
    - IPsec は，暗号技術を用いることで，IP パケット単位で改ざん検知や秘匿機能を提供するプロトコル
    - 