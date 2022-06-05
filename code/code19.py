nams = []
kent = []
age = []
num = ['1', '2', '3', '4']
for i in range(4):
    Nm = input(num[i]+'人目の名前を入力しましょう。\n')
    nams.append(Nm)

    Kn = input(nams[i]+'さんの出身地は（都道府県）？\n')
    kent.append(Kn)

    Nn = input(nams[i]+'さんの年齢は？\n')
    age.append(Nn)
else:
    print("入力された名前（リスト）",nams)
    print("入力された出身地（リスト）",kent)
    print("入力された年齢（リスト）",age)

    cov1 = set(nams)
    cov2 = set(kent)
    cov3 = set(age)

    print("入力された名前集合",cov1)
    print("入力された出身地集合",cov2)
    print("入力された年齢集合",cov3)
