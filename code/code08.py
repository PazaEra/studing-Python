N = list(range(1896,2020,4))

del N[5],N[10],N[10]
N.append(2021)

Tx = ["年は夏季オリンピックを開催しま","した。","せんでした。"]

string = int(input("西暦何年ですか？[1892～2021年]"))

if string in N:
    print(string,Tx[0],Tx[1])
else:
    print(string,Tx[0],Tx[2])