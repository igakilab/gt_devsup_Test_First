# gt_devsup_Test_First
実験1個目のプロダクト

プロダクト1つ目　三目並べ

三目並べとは、３×３のマスに二人が交互に○と×を書き込み、先に縦横斜めのいずれかでマークを揃えたら勝ちとなるゲームである。マルバツゲームとも呼ばれる。

今回は先行をプレイヤー(○)、後攻をコンピュータ(×)としてプログラムを作成する。

言語はPythonを使用し、以下の２つのファイルを作成する。

・sanmoku.py … ゲームの表示・進行・勝敗を行う。

・player.py  … プレイヤー・コンピュータの入力を行う。その際、コマをマスに置けるかも判断する。


各ファイルの仕様

sannmoku.pyの関数

・Judge … 指定したコマが揃っているかを確認する

引数 math:盤のリスト checkChara:揃っているかを確認するコマ

返り値 揃っている:True 揃っていない:False

・ShowMath … 盤を表示する

引数 math:盤のリスト

player.pyの関数

・CheckMath … 指定したマスに確認するコマが入っているかを確認する

引数 math:盤のリスト height,width:盤の位置 piece:確認するコマ

返り値 確認するコマが入っている:True その他:False

player.pyのクラス

・GamePlayer … プレイヤーの入力を行うクラス

・Computer　 … コンピュータの入力を行うクラス

GamePlayerクラスのメソッド

・Play … 盤にコマが置ける位置が指定されるまで回す。

引数 math:盤のリスト

返り値 盤の位置の添字（[縦,横]）

Computerクラスのメソッド

・Play … コンピュータにコマを置く位置を考えさせる

引数 math:盤のリスト

返り値 盤の位置の添字のリスト（[縦,横]）

・CheckWinner … リーチしているかを確認する

引数 math:盤のリスト player:確認するコマ

返り値 リーチしている:盤の位置の添字（[縦の添字,横の添字]） リーチなし:[-1,-1]

・IsReach … 指定した列がリーチ状態かを確認する

引数 math:盤のリスト piece:確認するコマ start:確認する列の初期位置 distance:列の間隔

返り値 リーチしている:空いている位置の添字（[縦,横]） リーチなし:[-1,-1]

--------------------------------------------------------------------------------------------------------

想定される作成順

sanmoku.py

1.Judgeの作成

2.表示機能の追加

3.現在の盤面を表示 

4.揃っているかの確認機能の追加


player.py

1.CheckMathの作成

2.自分のリーチ確認機能の追加

3.相手のリーチ確認機能の追加

4.IsReachメソッドの作成

*********************************************************************************************************
