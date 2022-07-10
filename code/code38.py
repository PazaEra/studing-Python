import csv

class Charactor:
    __slots__ = ['id', 'name', 'power', 'wiz', 'sta']

    def __init__(self, id, name, power, wiz, sta):
        self.id = id
        self.name = name
        self.power = power
        self.wiz = wiz
        self.sta = sta

    def show(self):
        print(f'{self.id}番の名前は{self.name}です。腕力は{self.power}、知力は{self.wiz}、体力{self.sta}です。')

class Competition:
    charactor = ['listcharactor']#リスト

    def charactor(self): #空のリスト?
        self.listCharactor = []

    def register_charactor(self, name): #キャラをリストに入れる。
        self.listCharactor.append(charactor)

    def show_charactor_list(self): #キャラリストの最終結果
        print('【参加者の一覧リスト】')
        for ch in self:
            print(ch[1])
#        for charactor in self.listcharactor:
#            print(charactor[1])

    def show_winner_arm(num):
        arm = []
        for i in range(5):
            arm.append(num[i][2])
            
        print('【腕相撲の結果】')
        for i in range(2):
            if num[i][2] >= num[i+1][2]:
                print(f'{num[i][1]}と{num[i+1][1]}の勝負は{num[i][1]}の勝ち')
            else:
                print(f'{num[i][1]}と{num[i+1][1]}の勝負は{num[i+1][1]}の勝ち')

        for i in range(2):
            if num[i+1][2] >= num[i+3][2]:
                print(f'{num[i+1][1]}と{num[i+3][1]}の勝負は{num[i+1][1]}の勝ち')
            else:
                print(f'{num[i][1]}と{num[i+3][1]}の勝負は{num[i+3][1]}の勝ち')
        print(f'腕相撲の優勝者は、腕力{num[4][2]}の{num[4][1]}さんです！')
                
    def show_winner_quiz(num):
        quiz = []
        for i in range(5):
            quiz.append(num[i][3])

        print('【クイズの結果】')
        for i in range(2):
            if num[i][3] >= num[i+2][3]:
                print(f'{num[i][1]}と{num[i+1][1]}の勝負は{num[i][1]}の勝ち')
            else:
                print(f'{num[i][1]}と{num[i+1][1]}の勝負は{num[i+1][1]}の勝ち')
                
        for i in range(2):
            if num[i][3] >= num[i+3][3]:
                print(f'{num[i][1]}と{num[i+3][1]}の勝負は{num[i][1]}の勝ち')
            else:
                print(f'{num[i][1]}と{num[i+3][1]}の勝負は{num[i+3][1]}の勝ち')
        print(f'クイズの優勝者は、知力{num[1][3]}の{num[1][1]}さんです！')        


    def show_winner_marathon(num):
        marathon = []
        for i in range(5):
            marathon.append(num[i][4])
            
        print('【マラソンの結果】')    
        for i in range(2):
            if num[i][4] >= num[i+1][4]:
                print(f'{num[i][1]}と{num[i+1][1]}の勝負は{num[i][1]}の勝ち')
            else:
                print(f'{num[i][1]}と{num[i+1][1]}の勝負は{num[i+1][1]}の勝ち')
                
        for i in range(2):
            if num[i+1][4] >= num[i+3][4]:
                print(f'{num[i+1][1]}と{num[i+3][1]}の勝負は{num[i+1][1]}の勝ち')
            else:
                print(f'{num[i][1]}と{num[i+3][1]}の勝負は{num[i][1]}の勝ち')
                
        print(f'マラソンの優勝者は、体力{num[1][4]}の{num[1][1]}さんです！')

GList = []
if __name__ == '__main__':
    competition = Competition()

    with open('CharactorList.csv','r', encoding='UTF-8') as file:
        reader = next(csv.reader(file))
        reader = csv.reader(file)
        for strList in reader:
            intId = int(strList[0])
            strName = strList[1]
            intPower = int(strList[2])
            intWiz = int(strList[3])
            intSta = int(strList[4])
            Charactor = Competition.show_charactor_list
            if intId % 2 == 0:
                GList.append(strList)

#print(GList)
Competition.show_charactor_list(GList)
Competition.show_winner_arm(GList)
Competition.show_winner_quiz(GList)
Competition.show_winner_marathon(GList)
