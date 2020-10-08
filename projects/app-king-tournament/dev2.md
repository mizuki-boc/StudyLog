## 開発ログ part2
___
- トピックに分けていろいろ書いていく

### スクリプトからオブジェクトにアタッチされた Rigid Body を読み込む方法
- スクリプトを直接アタッチする場合
    - スクリプトをオブジェクトに直接 DD
    - スクリプトでは
    `rb = GetComponent<Rigidbody>();`
    で読み込む
- 直接アタッチしない場合
    - `Unkart = GameObject.Find("Unkart");`
    のように、オブジェクトを Find して、
    `rb = Unkart.GetComponent<Rigidbody>();`
    インスタンス化したものから GetComponent メソッドを使うイメージ

### ボタンにスクリプトをアタッチする方法
- Hierarchy から button を作成
- Add Component から Event Trigger 追加
- Pointer Down とか Pointer Up とか任意のトリガーを選択する
- **空のオブジェクトを作成して、それにスクリプトをアタッチする**
- 空のオブジェクトを Event Trigger にアタッチする。
    - 空のオブジェクトを経由しないとアタッチできないことに注意

### 物体の当たり判定(Rigid Body) に関して
- Rigid Body の各プロパティの意味を解説しててわかりやすい
- 参考リンク
    - [物理エンジンと当たり判定を使いこなそう(その1)](http://inter-high-blog.unity3d.jp/2019/06/28/rigidbody/)