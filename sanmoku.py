﻿import player

#指定したコマが揃っているかの確認
#math:盤(2重リスト)　checkChara:確認するコマ
#return 揃っている:True 揃っていない:False
def Judge(math,checkChara):
    #if(math[0][0] == checkChara and math[0][1] == checkChara and math[0][2] == checkChara):

    return True


   if(math[1][0] == checkChara and math[1][1] == checkChara and math[1][2] == checkChara):

       return True


   if(math[2][0] == checkChara and math[2][1] == checkChara and math[2][2] == checkChara):

       return True


   if(math[0][0] == checkChara and math[1][0] == checkChara and math[2][0] == checkChara):

       return True


   if(math[0][1] == checkChara and math[1][1] == checkChara and math[2][1] == checkChara):

       return True


   if(math[0][2] == checkChara and math[1][2] == checkChara and math[2][2] == checkChara):

       return True


   if(math[0][0] == checkChara and math[1][1] == checkChara and math[2][2] == checkChara):

       return True


   if(math[0][2] == checkChara and math[1][1] == checkChara and math[2][0] == checkChara):
       return True


   return False



#盤を表示する
#math:盤(2重リスト)
def ShowMath(math):
    #追加タスク
    #for mathList in math:

        print(mathList)

if __name__ == "__main__":
    math = [["  " for i in range(3)] for j in range(3)]
    player = [player.GamePlayer(),player.Computer()]
    turn = 0
    winnerPlayer = -1

    #最初の盤の表示
    #ShowMath(math)

    #9ターン動かす
    for turn in range(9):

        #縦横の入力位置の取得
        height,width = player[turnPlayer].Play(math)

        #コマを盤に配置する
        #追加タスク
        #print("height = {0} width = {1}".format(height,width))

        math[height][width] = player[turnPlayer].mine

        #盤を表示する
        #ShowMath(math)

        #コマが揃っているか確認し、揃っていたらループを抜ける
        #if(winnerPlayer == -1):

        print("Draw")
    else:

        print("Winner {}".format(player[winnerPlayer].name))

    #勝利プレイヤーを表示
    #追加タスク
    #⑦
