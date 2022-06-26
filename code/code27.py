
Math = int(input('数学の点数(0-100の間の整数)を入力してください。\n'))

Eng = int(input('英語の点数(0-100の間の整数)を入力してください。\n'))

Jap = int(input('国語の点数(0-100の間の整数)を入力してください。\n'))

def create_ave_sum(intMath,intEng,intJap):
    all_point = intMath + intEng + intJap
    all_ave = (intMath + intEng + intJap) / 3
    return all_point, all_ave

write = create_ave_sum(Math, Eng, Jap)
ER = round(write[1],1)

print(f'全教科の点数は{write[0]}, 平均点は{ER}')