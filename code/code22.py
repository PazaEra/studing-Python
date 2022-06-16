import csv
import shutil

names = []
kents = []
scns = []
num = ['1', '2']
tex = []
for i in range(2):
    Nm = input(num[i]+'人目の名前を入力しましょう。\n')
    names.append(Nm)

    Kn = input(names[i]+'さんの出身地は（都道府県）？\n')
    kents.append(Kn)

    Nn = input(names[i]+'さんの学籍番号は？（半角英数で入力）\n')
    scns.append(Nn)
    
else:
    sump = []
    tx = ['名前','出身地','学籍番号']
    tx2 = [tx[0],tx[1],tx[2]]
    tex.append(tx2)
    ps = [names[0],kents[0],scns[0]]
    sump.append(ps)
    pq = [names[1],kents[1],scns[1]]
    sump.append(pq)
    print("入力された情報",sump)

with open('persondata.csv', 'w',encoding='UTF-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(tex)
    writer.writerows(sump)
    print("ファイルを書き込みました。\nファイルをコピーしました。")
shutil.copy("persondata.csv", "./persondata2.csv")
