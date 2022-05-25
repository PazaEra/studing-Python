st = int(input("整数："))

num = 1
total = 1

while num <= st:
    print("num = " + str(num))
    total *= num
    num += 1
    print("   ×")
else:
    print(st,"! =" + str(total))

print("End")
