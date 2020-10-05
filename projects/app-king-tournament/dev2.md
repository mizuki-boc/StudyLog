## 開発ログ part2
___
- トピックに分けていろいろ書いていく

### RigitBody をオブジェクトにアタッチする方法
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