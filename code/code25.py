import csv
import shutil
import re

ad01 = []
ad02 = []
ld01 = []
ld02 = []
am = []
latest = []
write_data = []

print("読み込んだリスト")
with open('dataset01.csv', 'r', encoding='UTF-8') as f:
    file_data = f.readlines()
    for line in file_data:
               ad01.append(line.replace("\n",""))

ld01.append(ad01[0].split(','))
ld01.append(ad01[1].split(','))
ld01.append(ad01[2].split(','))
print(ld01)

print("読み込んだリスト")
with open('dataset02.csv', 'r', encoding='UTF-8') as f:
    file_data = f.readlines()
    for line in file_data:
               ad02.append(line.replace("\n",""))

ld02.append(ad02[0].split(','))
ld02.append(ad02[1].split(','))
ld02.append(ad02[2].split(','))
print(ld02)

print("連結したリスト")
am.append(ad01[0].split(','))
am.append(ad01[1].split(','))
am.append(ad01[2].split(','))
am.append(ad02[0].split(','))
am.append(ad02[1].split(','))
am.append(ad02[2].split(','))
print(am)

print("用語置き換え後のリスト")
am.sort(reverse=False)
amod1 = re.sub('ITエンジニア|プログラマー|SE',"技術者",am[0][2])
amod3 = re.sub('ITエンジニア|プログラマー|SE',"技術者",am[2][2])
amod4 = re.sub('ITエンジニア|プログラマー|SE',"技術者",am[3][2])
amod5 = re.sub('ITエンジニア|プログラマー|SE',"技術者",am[4][2])
amod6 = re.sub('ITエンジニア|プログラマー|SE',"技術者",am[5][2])

ap1 = [am[0][0],am[0][1],amod1]
ap2 = [am[1][0],am[1][1],am[1][2]]
ap3 = [am[2][0],am[2][1],amod3]
ap4 = [am[3][0],am[3][1],amod4]
ap5 = [am[4][0],am[4][1],amod5]
ap6 = [am[5][0],am[5][1],amod6]

latest.append(ap1)
latest.append(ap2)
latest.append(ap3)
latest.append(ap4)
latest.append(ap5)
latest.append(ap6)
print(latest)

#カウント
A1 = amod1.count('。')#016
A2 = amod3.count('。')#033
A3 = amod4.count('。')#036
A4 = amod5.count('。')#040
A5 = amod6.count('。')#043

print(am[0][0],"の書いた文章数は",A1)
print(am[1][0],"の書いた文章数は","0")
print(am[2][0],"の書いた文章数は",A2)
print(am[3][0],"の書いた文章数は",A3)
print(am[4][0],"の書いた文章数は",A4)
print(am[5][0],"の書いた文章数は",A5)

print("削除候補は",am[1])
del am[0]
print(am)
