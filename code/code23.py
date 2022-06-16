import csv
import shutil
import re

all_data = []
latest_data = []

write_data = []

print("ファイルを読み込みました。")
with open('persondata2.csv', 'r', encoding='UTF-8') as f:
    file_data = f.readlines()
    for line in file_data:
               all_data.append(line.replace("\n",""))
               
latest_data.append(all_data[0].split(','))
latest_data.append(all_data[1].split(','))
latest_data.append(all_data[2].split(','))
print(latest_data)

print(latest_data[1][0])
str1 = latest_data[1][2]
str2 = latest_data[2][2]
print("入学年記号",str1[:2])
print("学科記号",str1[2:5])
print("3桁番号",str1[5:])
print(latest_data[2][0])
print("入学年記号",str2[:2])
print("学科記号",str2[2:5])
print("3桁番号",str2[5:])
