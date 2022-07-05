from code33_c2p31087 import create_subject_list 
from code33_c2p31087 import search_class_match_word
from code33_c2p31087 import search_subject_include_word
import unicodedata
import requests

als = []
if __name__ == '__main__':
    url_1 = 'https://www.bunkyo.ac.jp/faculty/fac-info/information-systems/curriculum.html'
    url_2 = 'https://www.bunkyo.ac.jp/faculty/fac-info/information-society/curriculum.html'
    url_3 = 'https://www.bunkyo.ac.jp/faculty/fac-info/media-and-communication/curriculum.html'
listSys = create_subject_list(requests.get(url_1))
listSoc = create_subject_list(requests.get(url_2))
listMed = create_subject_list(requests.get(url_3))
als.extend(listSys)
als.extend(listSoc)
als.extend(listMed)

SSl = ['システム開発領域科目', '情報デザイン領域科目', '計算社会科学領域科目', 'プロジェクトマネジメント領域科目', 'ソーシャルメディア領域科目', 'マスメディア領域科目']
WWR = []
fs = int(input("領域で検索する場合は0、科目で検索する場合は1、を入力してください。\n"))
if fs == 0:
    print("検索したい領域番号を入力してください。")
    ser = int(input("システム開発領域科目：0\n情報デザイン領域科目：1\n計算社会科学領域科目：2\nプロジェクトマネジメント領域科目：3\nソーシャルメディア領域科目：4\nマスメディア領域科目：5\n"))
    scv = SSl[ser]
    ser_list = search_class_match_word(scv,als)
    ct1 = len(ser_list)
    for i in range(ct1):
        print(f'領域：{ser_list[i][0]},科目：{ser_list[i][1]}')

if fs == 1:
    wor = input('検索ワードを入力してください。\n')
    wor_list = search_subject_include_word(wor,als)
    ct2 = len(wor_list)
    for i in range(ct2):
        print(f'領域：{wor_list[i][0]},科目：{wor_list[i][1]}')

