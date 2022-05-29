while True:
    Nm = input("ローマ字で名と姓を入力してさい。\n名と姓の間に半角スペースを入れてください。\nまた、文字数は25文字以内です。\n")
    spc = ' '
    if Nm.isascii():
        if len(Nm) <= 25:
            if spc in Nm:
                Dz = list(Nm.split())
                print("姓は",Dz[1])
                print("名は",Dz[0])
                break
