SN = int((input("商品の値段を入力してください[円]:")))
SK = int((input("預かった金額を入力してください[円]:")))

#おつり
Ot = SK - SN

MB = Ot % 5000
MD = MB % 1000
MF = MD % 500
MH = MF % 100
MJ = MH % 50
ML = MJ % 10
MN = ML % 5

MA = Ot // 5000
MC = MB // 1000
ME = MD // 500
MG = MF // 100
MI = MH // 50
MK = MJ // 10
MM = ML // 5
MO = MN // 1

Tx = ["おつりは","5000円札は","1000円札は","500円玉は","100円玉は","50円玉は"
      ,"10円玉は","5円玉は","1円玉は","枚です。","円です。"]

print(Tx[0],Ot,Tx[10])
print(Tx[1],MA,Tx[9])
print(Tx[2],MC,Tx[9])
print(Tx[3],ME,Tx[9])
print(Tx[4],MG,Tx[9])
print(Tx[5],MI,Tx[9])
print(Tx[6],MK,Tx[9])
print(Tx[7],MM,Tx[9])
print(Tx[8],MO,Tx[9])