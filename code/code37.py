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
            print(ch)
#        for charactor in self.listcharactor:
#            print(charactor[1])
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
                GList.append(strName)

Competition.show_charactor_list(GList)
