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
        
def KMP(x,m,y,n):
    KmpNext = [-1 for i in range(m + 1)]

    preKMP(x,m,KmpNext)

    i = j = 0
    while j < n:
        if i > -1 and x[i] != y[j] and j >= n - m:
            # print(f"Dịch 1 khoảng = {i - KmpNext[i]} ({i} - {KmpNext[i]})")
            break
        while i > -1 and x[i] != y[j]:
            # print(f"Dịch 1 khoảng = {i - KmpNext[i]} ({i} - {KmpNext[i]})")
            i = KmpNext[i]
        i += 1
        j += 1
        if i >= m:
            print(f"Vị trí {j - i} xuất hiện vị trí của xâu x trong y")
            # print(f"Dịch 1 khoảng = {i - KmpNext[i]} ({i} - {KmpNext[i]})")
            i = KmpNext[i]

x = 'GCAGAGAG'
y = 'GCATCGCAGAGAGTATACAGTACG'
m = len(x)
n = len(y)
KMP(x,m,y,n)