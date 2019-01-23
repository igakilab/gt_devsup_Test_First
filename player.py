from abc import ABCMeta,abstractmethod

#指定マスが指定した状態か確認
#math:盤(2重リスト) height:縦の添字 width:横の添字 piece:確認するコマ
#return 空いている:True 空いていない:False
def CheckMath(math,height,width,piece):
    #①

class Player(metaclass=ABCMeta):
    @abstractmethod
    def Play(self,math):
        pass

#プレイヤーのクラス
class GamePlayer(Player):
    def __init__(self):
        self.mine = "○"
        self.name = "player"
        self.inputExample = [["00","01","02"],["10","11","12"],["20","21","22"]]

    #コマの配置入力
    def Play(self,math):
        print("プレイヤーの入力")
        #入力例の出力
        for example in self.inputExample:
            print(example)

        while (True):
            #キー入力
            inputData = input()

            height = int(inputData) // 10
            width  = int(inputData) % 10

            #コマが置けるかの確認/置けるならその位置を返す
            #②

#コンピュータのクラス
class Computer(Player):
    def __init__(self):
        self.mine = "×"
        self.name = "Computer"
        self.player = "○"
        self.priority = [[1,1],[0,0],[0,2],[2,0],[2,2],[0,1],[1,0],[1,2],[2,1]]

    #コマの配置入力
    def Play(self,math):
        print("コンピュータの入力")

        #自分がリーチしているか確認/置けるならその位置を返す
        #③

        #相手がリーチしているか確認/置けるならその位置を返す
        #④

        #どちらもリーチでない場合優先順位でコマを置く
        for i in range(9):
            if(CheckMath(math,self.priority[i][0],self.priority[i][1],"  ")):
                return self.priority[i]

    #リーチしているかの確認
    #math:盤(2重リスト) player:確認するプレイヤーのコマ
    #return リーチしていたら空いている場所のリストを返す リーチしていなかったら[-1,-1]を返す
    def CheckWinner(self,math,player):
        #IsReachで各列のリーチを確認する/置けるならその位置を返す
        inputData = self.IsReach(math,player,[0,0],[1,1])
        if(not inputData == [-1,-1]):
            return inputData
        #⑤        
        return [-1,-1]

    #指定した列がリーチしているかの確認
    #math:盤(2重リスト) piece:コマ start:列の初期位置 distance:列の間隔
    #return リーチしていたら空いている場所のリストを返す リーチしていなかったら[-1,-1]を返す
    def IsReach(self,math,piece,start,distance):
        checkMath = start
        pieceCount = 0
        result = []
        #各マスを確認し、pieceと同じならpieceCountに１を足す。空マスならその位置を取る。
        #pieceCountが2かつ空マスがあるなら空マスの位置を返す
        #⑥
