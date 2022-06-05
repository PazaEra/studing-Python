names = []
kents = []
ages = []
num = ['1', '2', '3', '4']
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

keag = zip(kents,ages)    
ast = dict(zip(names,keag))
print(ast)

ser = input('検索したい名前は？\n')
if ser in names:
    sh = ast.get(ser)[0:4]
    nn = ast.get(ser)[1:2]
    print("出身地は",sh,"です")
    print("年齢は",nn,"です")
    
