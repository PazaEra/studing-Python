import random

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
    intId = 1
    strName = input('あなたの名前を教えてください。')
    intPower = random.randint(1,10)
    intWiz = random.randint(1,10)
    intSta = random.randint(1,10)

    charactor = Charactor(intId, strName, intPower, intWiz, intSta)
    charactor.show()


        
