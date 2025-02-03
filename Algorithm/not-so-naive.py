def NSN(x,m,y,n):
    j,k,ell = 0,0,0
    if x[0] == x[1]:
        k = 2
        ell = 1
    else:
        k = 1
        ell = 2
    while j <= n - m:
        if x[1] != y[j + 1]:
            j += k
        else:
            if x[2 : m] == y[j + 2 : j + m] and x[0] == y[j]:
                print(f"Vị trí {j} xuất hiện vị trí của xâu x trong y")
            j += ell

x = 'GCAGAGAG'
y = 'GCATCGCAGAGAGTATACAGTACG'
m = len(x)
n = len(y)
NSN(x,m,y,n)