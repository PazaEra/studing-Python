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
        for charactor in self.listcharactor:
            print(self.listcharactor)

if __name__ == '__main__':
    competition = Competition()

    with open('CharactorList.csv','r', encoding='UTF-8') as file:
        reader = next(csv.reader(file))
        reader = csv.reader(file)
        #l = [row for row in reader]
        for strList in reader:
            intId = Charactor.id
            strName = Charactor.name
            intPower = Charactor.power
            intWiz = Charactor.wiz
            intSta = Charactor.sta
            #キャラクタクラスのインスタンスを作成
            Charactor = competition.show_charactor_list(self.name)
        # 競技大会のインスタンスにIDが偶数番号のキャラクタのインスタンスを登録
        if Charactor.id % 2 == 0:
            competition.show_charactor_list(strName)
    

    competition.show_charactor_list()
