## デバッグエラーログ
- プレイヤーとディーラー両方バーストしたとき
```
------------------------ GAME START ------------------------
bet amount = [100]
Insurance ? - y/n
insurance rejected!
===  mizuki s turn ! ===
[312, 104]
Hit = h key
Stand = s key
Double down = d key
Surrender = u key
===  mizuki s turn ! ===
[312, 104, 302]
Hit = h key
Stand = s key
mizuki burst !
dealer hand [201, 203, 302, 309, 210] => スコア 25 
mizuki [[312, 104, 302, 213]]         => スコア 26
push                                  => プレイヤーの負けになるべき
mizuki s income 0
mizuki s bankroll 1000
```