import time
from bs4 import BeautifulSoup
import unicodedata
import requests
import asyncio
from utile import create_subject_list


start = time.time()


if __name__ == '__main__':
    url_1 = '.html'
    url_2 = '.html'
    url_3 = '.html'
listSys = create_subject_list(requests.get(url_1))
listSoc = create_subject_list(requests.get(url_2))
listMed = create_subject_list(requests.get(url_3))

    
end = time.time()
print(f'通信時間: {end - start}\n')

ct1 = len(listSys)
ct2 = len(listSoc)
ct3 = len(listMed)
print("【〇〇学科の専門領域科目リスト】")
for i in range(ct1):
    print(f'領域：{listSys[i][0]},科目：{listSys[i][1]}')
    
print("\n【〇〇学科の専門領域科目リスト】")
for i in range(ct2):
    print(f'領域：{listSoc[i][0]},科目：{listSoc[i][1]}')

print("\n【〇〇学科の専門領域科目リスト】")
for i in range(ct3):
    print(f'領域：{listMed[i][0]},科目：{listMed[i][1]}')
