import datetime

while True:
    Nm = input("ローマ字で名と姓を入力してさい。\n名と姓の間に半角スペースを入れてください。\nまた、文字数は25文字以内です。\n")
    spc = ' '
    if Nm.isascii():
        if len(Nm) <= 25:
            if spc in Nm:
                Dz = list(Nm.split())
                dt_now_jst = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
                print("姓は",Dz[1].upper(),"、名は",Dz[0].capitalize(),"です。")
                print(dt_now_jst.strftime('%Y年%m月%d日%H時%M分に入力完了しました。'))
                break
