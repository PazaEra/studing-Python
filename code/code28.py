all_data = []
latest_data = []
update_data = []
CT = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ctuj = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
cut = [0, 1, 2]
AC = []
AR = []

with open('file10-1.csv', 'r',encoding='UTF-8',newline='') as f:
    file_data = f.readlines()
    for line in file_data:
        latest_data.append(line.replace("\r\n",""))
    
for i in range(11):
    all_data.append(latest_data[i].split(','))

def create_ave_sum(intMath,intEng,intJap):
    all_point = intMath + intEng + intJap
    all_ave = (intMath + intEng + intJap) / 3
    return all_point, all_ave

del all_data[0]
ad0 = list(map(int, all_data[0]))
ad1 = list(map(int, all_data[1]))
ad2 = list(map(int, all_data[2]))
ad3 = list(map(int, all_data[3]))
ad4 = list(map(int, all_data[4]))
ad5 = list(map(int, all_data[5]))
ad6 = list(map(int, all_data[6]))
ad7 = list(map(int, all_data[7]))
ad8 = list(map(int, all_data[8]))
ad9 = list(map(int, all_data[9]))

CAS1 = create_ave_sum(ad0[0], ad0[1], ad0[2])
CAS2 = create_ave_sum(ad1[0], ad1[1], ad1[2])
CAS3 = create_ave_sum(ad2[0], ad2[1], ad2[2])
CAS4 = create_ave_sum(ad3[0], ad3[1], ad3[2])
CAS5 = create_ave_sum(ad4[0], ad4[1], ad4[2])
CAS6 = create_ave_sum(ad5[0], ad5[1], ad5[2])
CAS7 = create_ave_sum(ad6[0], ad6[1], ad6[2])
CAS8 = create_ave_sum(ad7[0], ad7[1], ad7[2])
CAS9 = create_ave_sum(ad8[0], ad8[1], ad8[2])
CAS10 = create_ave_sum(ad9[0], ad9[1], ad9[2])

AC.append(CAS1[0])
AC.append(CAS2[0])
AC.append(CAS3[0])
AC.append(CAS4[0])
AC.append(CAS5[0])
AC.append(CAS6[0])
AC.append(CAS7[0])
AC.append(CAS8[0])
AC.append(CAS9[0])
AC.append(CAS10[0])

R1 = round(CAS1[1],1)
R2 = round(CAS2[1],1)
R3 = round(CAS3[1],1)
R4 = round(CAS4[1],1)
R5 = round(CAS5[1],1)
R6 = round(CAS6[1],1)
R7 = round(CAS7[1],1)
R8 = round(CAS8[1],1)
R9 = round(CAS9[1],1)
R10 = round(CAS10[1],1)

AR.append(R1)
AR.append(R2)
AR.append(R3)
AR.append(R4)
AR.append(R5)
AR.append(R6)
AR.append(R7)
AR.append(R8)
AR.append(R9)
AR.append(R10)

for i in range(10):
    print(f'{ctuj[i]}人目の全教科の合計点は{AC[i]},平均点は{AR[i]}です')  
