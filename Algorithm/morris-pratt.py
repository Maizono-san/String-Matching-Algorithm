def preMP(x,m,mpNext):
    i = 0
    j = mpNext[0]
    while i < m:
        while j > -1 and x[i] != x[j]:
            j = mpNext[j]    
            
        i += 1
        j += 1
        mpNext[i] = j

def MP(x,m,y,n):
    mpNext = [-1 for i in range(m + 1)]

    preMP(x,m,mpNext)

    i = j = 0
    while j < n:
        if i > -1 and x[i] != y[j] and j >= n - m:
            print(f"Dịch 1 khoảng = {i - mpNext[i]} ({i} - {mpNext[i]})")
            break
        while i > -1 and x[i] != y[j]:
            print(f"Dịch 1 khoảng = {i - mpNext[i]} ({i} - {mpNext[i]})")
            i = mpNext[i]
        i += 1
        j += 1
        if i >= m:
            print(f"Vị trí {j - i} xuất hiện vị trí của xâu x trong y")
            print(f"Dịch 1 khoảng = {i - mpNext[i]} ({i} - {mpNext[i]})")
            i = mpNext[i]

x = 'GCAGAGAG'
y = 'GCATCGCAGAGAGTATACAGTACG'
m = len(x)
n = len(y)
MP(x,m,y,n)

