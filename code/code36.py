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
        l = [row for row in reader]
        for i in range(10):
            intId = int(l[i][0])
            strName = l[i][1]
            intPower = int(l[i][2])
            intWiz = int(l[i][3])
            intSta = int(l[i][4])
            person = Charactor(intId, strName, intPower, intWiz, intSta)
            person.show()
