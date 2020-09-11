## デバッグエラーログ
- プレイヤーとディーラー両方バーストしたとき(修正済み)
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

- スプリット時に　４回勝ったことになる(修正済み)
```
- case 1
------------------------ GAME START ------------------------
bet amount = [100]
split? - y/n
[[208, 408], [208, 108]]
[208, 408]
[208, 108]
dealer hand [112, 303, 108]
mizuki [[208, 408], [208, 108]]
mizuki lose!
mizuki lose!
mizuki lose!
mizuki lose!
mizuki s income -400
mizuki s bankroll 600
```
```
- case 2
------------------------ GAME START ------------------------
bet amount = [100]
split? - y/n
[[101, 413], [101, 313]]
[101, 413]
[101, 313]
dealer hand [308, 209]
mizuki [[101, 413], [101, 313]]
mizuki s win!
mizuki s win!
mizuki s win!
mizuki s win!
mizuki s income 400
mizuki s bankroll 1400
```
```
- case 3
------------------------ GAME START ------------------------
bet amount = [100]
Insurance ? - y/n
insurance accepted!
split? - y/n
[[310, 308], [210, 302]]
[310, 308]
[210, 302, 105]
dealer hand [101, 106]
mizuki [[310, 308], [210, 302, 105]]
mizuki s win!
push
mizuki s win!
push
mizuki s income 100
mizuki s bankroll 1100
```