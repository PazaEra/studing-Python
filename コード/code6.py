SA = int((input("整数aを入力してください:")))
SB = int((input("整数bを入力してください:")))

P = SA + SB
M = SA - SB
K = SA * SB
W = SA // SB
W2 = SA % SB 

Tx = ["aとbの和は","aとbの差は","aとbの積は","aとbの商は","余りは"]

print(Tx[0],P,"です。")
print(Tx[1],abs(M),"です。")
print(Tx[2],K,"です。")
print(Tx[3],W,"で",Tx[4],W2,"です。")


