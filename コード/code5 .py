A = float(input("身長を入力してください[m]:"))
X = float(input("体重を入力してください[kg]:"))

BMI = X / A ** 2
IBW = A ** 2 * 22

T = ["あなたのBMI値は","で,適正体重は","kgです。"]

print(T[0], round(BMI,2), T[1], round(IBW,2), T[2])