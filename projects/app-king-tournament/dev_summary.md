# アプリ王選手権に参加しての総括

## TL;DR
- アプリ王選手権に参加した時の良かった点、よくなかった点を書く。
- それを踏まえて、第三回(あるか知らんけど)や、次回の開発の糧にしたい...

## モチベーション維持に関して
- 良かった点
    - issue でやるべきことが明確になっていたので、中だるみすることはなかった(APEX をのぞく)
- よくなかった点
    - 開発にあたって、モチベーションの維持がめちゃくちゃ難しかった。特に開発中に APEX にドはまりして、ほとんど開発していない期間が発生した。
        - 締め切り直前に急いで実装して、何とか間に合わせた感じ。
    - 提出後、最新の BS では起動しない問題が発生した。原因は今もイマイチわかってないが、先にひな形を作って、**バックアップとりつつ**、重要性の高いタスクから処理していく必要がある。

## github issue を使った
- 今回は、devlog をつけるのではなく、github の issue でタスク管理を行った。
- 良かった点
    - 処理するべきタスクが可視化され、何やったらいいかワカラン状態になることがほぼなかった。
    - **BS で起動できない問題**が発生したとき、unity version 2019 で作り直す必要があったが、過去のissue を見ることでサクサク解決することができた。
- 良くなかった点
    - タスクの重要度管理ができていなかった。めんどくさい実装(DB 連携、UIなど)がどんどん後回しになり、逆にカートの挙動(大事だけど)とかいじりすぎた。(の割にバグある。)
        - 次回つくる機会があれば、そのへんも考慮しつつ開発したい。(調べると、github のみでタスク管理とか全部やってる[記事](https://qiita.com/itkr/items/0d4c0015da28827b2bb7)とか散見したので、参考にしたい。)
        - トップレベルの優先度のタスクを完了しないと、下位レベルのタスクに着手しない、的なルールを設けると効率よく開発できそう。(な気がする)
    
## 必要要件の設定に関して
- アプリに必要な機能、機能というか、**加藤純一のゲームであること、その面白さ**(普通のレースゲームとの違い。ストロングポイント。)の設定が不十分だったと反省。
    - **面白さ、どこを面白いと感じさせるか設定することは実際めちゃくちゃ大事だと感じた。** 例えばオセロは神ゲーだが、今 AppStore にオセロのゲームをあげても DL されないと考えられる。
- カートの挙動とか、レースゲームとして必要な機能も実装する必要はもちろんあるが、ユーザ(今回の場合は、うんこちゃんと視聴者)に楽しんでもらう必要がある。という点をもっと配慮すべきだった。
- 例えば、配信中のコメントを YTAPI で取得して、ゲーム内に登場させる、、とかの機能は欲しかったかもしれない。

## 放送を見終えて
- レベル高すぎ。
- 60 エントリくらいあって、下から4番目くらいだった;;

## まとめ
- やめそうになったけど、最後まで続けてよかった
    - **BS 最新版で起動できない問題** が意味不すぎて、詰みかけたけど、プレイできる状態にまでもっていけてよかった。
- タスク管理をもっとちゃんとするべき
- UI, BGM とかの充実