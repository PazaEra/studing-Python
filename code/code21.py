names = []
kents = []
ages = []
num = ['1', '2', '3', '4']
mt = []
for i in range(4):
    Nm = input(num[i]+'人目の名前を入力しましょう。\n')
    names.append(Nm)

    Kn = input(names[i]+'さんの出身地は（都道府県）？\n')
    kents.append(Kn)

    Nn = input(names[i]+'さんの年齢は？\n')
    ages.append(Nn)
else:
    print("入力された名前（リスト）",names)
    print("入力された出身地（リスト）",kents)
    print("入力された年齢（リスト）",ages)
    
    cov1 = set(names)
    cov2 = set(kents)
    cov3 = set(ages)
    print("入力された名前集合",cov1)
    print("入力された出身地集合",cov2)
    print("入力された年齢集合",cov3)

nf = [names[0],[kents[0],ages[0]]]
ns = [names[1],[kents[1],ages[1]]]
nt = [names[2],[kents[2],ages[2]]]
nq = [names[3],[kents[3],ages[3]]]
mt.append(nf)
mt.append(ns)
mt.append(nt)
mt.append(nq)
print(mt)

ct = dict(mt)

ser = input('検索したい名前は？\n')
if ser in names:
    sh = ct.get(ser)[0:2]
    nn = ct.get(ser)[1:2]
    print("出身地は",sh,"です")
    print("年齢は",nn,"です")
    
