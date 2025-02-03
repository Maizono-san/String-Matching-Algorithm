def BF(x,m,y,n):
    for j in range(0, n - m + 1):
        if x == y[j:j+m]:
            print(f"Vị trí {j} xuất hiện vị trí của xâu x trong y")

x = 'GCAGAGAG'
y = 'GCATCGCAGAGAGTATACAGTACG'
m = len(x)
n = len(y)
BF(x,m,y,n)