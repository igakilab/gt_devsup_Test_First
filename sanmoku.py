import player

#指定したコマが揃っているかの確認
#math:盤(2重リスト)　checkChara:確認するコマ
#return 揃っている:True 揃っていない:False
def Judge(math,checkChara):
    #①

#盤を表示する
#math:盤(2重リスト)
def ShowMath(math):
    #追加タスク
    #②

if __name__ == "__main__":
    math = [["  " for i in range(3)] for j in range(3)]
    player = [player.GamePlayer(),player.Computer()]
    turn = 0
    winnerPlayer = -1

    #最初の盤の表示
    #③

    #9ターン動かす
    for turn in range(9):

        #縦横の入力位置の取得
        height,width = player[turnPlayer].Play(math)

        #コマを盤に配置する
        #追加タスク
        #④

        #盤を表示する
        #⑤

        #コマが揃っているか確認し、揃っていたらループを抜ける
        #⑥

    #勝利プレイヤーを表示
    #追加タスク
    #⑦
