import random

Nm = []
Ar = []
Br = []
En = []
ch1 = []
ch2 = []
ch3 = []
all_ch = []
prg = ['腕相撲','クイズ','マラソン']
cun = ['1','2','3']

for i in range(3):
    k1 = input(cun[i]+"人目のキャラクタの名前入力：")
    Nm.append(k1)
    
    r_arm = random.randrange(1,11)
    Ar.append(r_arm)

    r_brains = random.randrange(1,11)
    Br.append(r_brains)

    r_energy = random.randrange(1,11)
    En.append(r_energy)


ch1 = [Nm[0],Ar[0],Br[0],En[0]]
ch2 = [Nm[1],Ar[1],Br[1],En[1]]
ch3 = [Nm[2],Ar[2],Br[2],En[2]]
all_ch = [ch1,ch2,ch3]
print(all_ch)

print(Nm[0],"のパラメータ")
print("腕力：",Ar[0],"知力：",Br[0],"体力：",En[0])
print(Nm[1],"のパラメータ")
print("腕力：",Ar[1],"知力：",Br[1],"体力：",En[1])
print(Nm[2],"のパラメータ")
print("腕力：",Ar[2],"知力：",Br[2],"体力：",En[2])
print("腕力の最大値：",max(Ar))
print("知力の最大値：",max(Br))
print("体力の最大値：",max(En))

VSna = random.sample(all_ch,2)
ct = [0, 1, 2,]

ctran = random.sample(ct,1)
V = ctran[0]
J = V + 1

print(VSna[0][0],"と",VSna[1][0],"で",prg[V],"勝負！")

fst = VSna[0][J]
sec = VSna[1][J]

if fst == sec:
    print("引き分け")
else:
    if fst >= sec:
        print(VSna[0][0],"の勝ち")
    else:
        print(VSna[1][0],"の勝ち")
