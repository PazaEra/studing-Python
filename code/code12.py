s = int(input('2以上の自然数n＞'))

    
for i in range(2, s):
    F = list(range(2, s))
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=' ')

print(' ')
print('100までの素数は',len(F),'個です。')
