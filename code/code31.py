import time
from bs4 import BeautifulSoup
import unicodedata
import requests
import asyncio
from utile import create_subject_list

start = time.time()

if __name__ == '__main__':
    url = '.html'
    listSys = create_subject_list(requests.get(url))
    
end = time.time()

print(f'通信時間: {end - start}\n')

ct = len(listSys)
print("【〇〇学科の専門領域科目リスト】")
for i in range(ct):
    print(f'領域：{listSys[i][0]},科目：{listSys[i][1]}')
    
