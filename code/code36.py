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


if __name__ == '__main__':

    with open('CharactorList.csv','r', encoding='UTF-8') as file:
        reader = next(csv.reader(file))
        reader = csv.reader(file)
        for strList in reader:
            intId = int(strList[0])
            strName = strList[1]
            intPower = int(strList[2])
            intWiz = int(strList[3])
            intSta = int(strList[4])
            person = Charactor(intId, strName, intPower, intWiz, intSta)
            person.show()
