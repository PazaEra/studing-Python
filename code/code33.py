from bs4 import BeautifulSoup
import unicodedata
import requests

#領域
def search_class_match_word(numf,alsn):
    lastF = [s for s in alsn if numf in s]
    return lastF
#科目
def search_subject_include_word(nums,alsm):
    lastS = [s for s in alsm if nums in s]
    return lastS
#Test
def create_subject_list(html):
    soup = BeautifulSoup(html.content, "html.parser")
    class_name = ''
    sub_name = ''
    output_list = []
    class_list = ['システム開発領域科目', '情報デザイン領域科目'
                  , '計算社会科学領域科目', 'プロジェクトマネジメント領域科目'
                  , 'ソーシャルメディア領域科目', 'マスメディア領域科目']
    proc_flg = False

    for element in soup.find_all("tr"):
        for element2 in element.find_all("th"):
            if element2.text in class_list:
                class_name = element2.text
                class_name = unicodedata.normalize("NFC", class_name)
                proc_flg = True
            else:
                proc_flg = False
        for element2 in element.find_all("td"):
                if element2 != '' and proc_flg == True:
                    sub_name = element2.text
                    output_list.append([class_name, sub_name])

    return output_list
