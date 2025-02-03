def preKMP(x,m,KmpNext):
    i = 0
    j = KmpNext[0]
    while i < m:
        while j > -1 and x[i] != x[j]:
            j = KmpNext[j]    
            
        i += 1
        j += 1
        if i < m and x[i] == x[j]:
            KmpNext[i] = KmpNext[j]
        else:
            KmpNext[i] = j

def AXAMAC(x,m,y,n):
    KmpNext = [-1 for i in range(m + 1)]

    preKMP(x,m,KmpNext)

    ell = 1

    while ell < m:
        if x[ell - 1] != x[ell]:
            break
        else:
            ell += 1

    if ell == m:
        ell = 0
    
    i = ell
    j,k = 0,0

    while j <= n - m:
        while i < m and x[i] == y[i + j]:
            i += 1
        if i >= m:
            while k < ell and x[k] == y[j + k]:
                k += 1
            if k >= ell:
                print(f"Vị trí {j} xuất hiện vị trí của xâu x trong y")
        j += i - KmpNext[i]
        print(f"Dịch 1 khoảng = {i - KmpNext[i]} ({i} - {KmpNext[i]})")
        if i == ell:
            k = max(0, k - 1)
        else:
            if KmpNext[i] <= ell:
                k = max(0,KmpNext[i])
                i = ell
            else:
                k = ell
                i = KmpNext[i]

x = 'GCAGAGAG'
y = 'GCATCGCAGAGAGTATACAGTACG'
m = len(x)
n = len(y)
AXAMAC(x,m,y,n)