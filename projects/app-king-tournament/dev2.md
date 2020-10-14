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

### Prefab に関して
- オブジェクト指向言語でいう、クラスが Prefab にあたる。
- Unity の Scene 上で作成したオブジェクトは、インスタンスであり、Prefab を用いることで同一の性質を持ったオブジェクトを複数生成できる

### Unity の画面遷移実装に関して
- 画面遷移実装方法に関してはいろいろあるらしい
- 参考
    - [[Unity初心者Tips]画面を切り替える3つの方法](https://qiita.com/JunShimura/items/d5ffae65b7fbbcc95ce9)

### FixedUpdate 関数と Update 関数の違いに関して
- Update 関数
    - 毎フレーム呼ばれる
- FixedUpdate 関数
    - 呼ばれる間隔を指定できる
- 入力アクションなど、リアルタイム性が高く求められる処理は Update 関数を使う