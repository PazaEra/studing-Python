S = [1.68, 1.72, 1.71, 1.69, 1.65]
T = [63, 67, 79, 58, 63]

BMI0 = T[0]/S[0]**2
IBW0 = S[0]**2*22
BMI1 = T[1]/S[1]**2
IBW1 = S[1]**2*22
BMI2 = T[2]/S[2]**2
IBW2 = S[2]**2*22
BMI3 = T[3]/S[3]**2
IBW3 = S[3]**2*22
BMI4 = T[4]/S[4]**2
IBW4 = S[4]**2*22

BMIA = [BMI0,BMI1,BMI2,BMI3,BMI4]
A = sum(BMIA) / len(BMIA)
BMIM0 = max(BMIA)
BMIM1 = BMIA.index(max(BMIA))+1
BMIN0 = min(BMIA)
BMIN1 = BMIA.index(min(BMIA))+1

X = ["人目のBMI値は","で,適正体重は","kgです。","BMI値の","番目の人です。","平均値は","最大値は","最小値は"]

print("1",X[0],BMI0,X[1],IBW0,X[2])
print("2",X[0],BMI1,X[1],IBW1,X[2])
print("3",X[0],BMI2,X[1],IBW2,X[2])
print("4",X[0],BMI3,X[1],IBW3,X[2])
print("5",X[0],BMI4,X[1],IBW4,X[2])
print(X[3],X[5],A,"です。")
print(X[3],X[6],BMIM0,"で",BMIM1,X[4])
print(X[3],X[7],BMIN0,"で",BMIN1,X[4])