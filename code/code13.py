st = int(input("何項目？＞"))

def F1(Nm):
    a, b = 1, 0
    for _ in range(Nm):
        a, b = a + b, a
    return b

if __name__ == "__main__":
    print("第",st,"項目は",F1(st),"です。")









