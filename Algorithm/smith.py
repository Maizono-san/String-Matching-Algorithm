def preBmBc(x):
    ASIZE = 256  # Assuming ASCII characters
    m = len(x)
    bmBc = [m] * ASIZE
    for i in range(m - 1):
        bmBc[ord(x[i])] = m - i - 1
    return bmBc
 
def preQsBc(x):
    ASIZE = 256  # Assuming ASCII characters
    m = len(x)
    qsBc = [m+1] * ASIZE
    for i in range(m):
        qsBc[ord(x[i])] = m - i
    return qsBc
 
def S(x, y, m ,n):
    bmBc = preBmBc(x)
    qsBc = preQsBc(x)
   
    j = 0
    while j <= n - m:
        if x == y[j : j + m]:
            print(f"Vị trí {j} xuất hiện vị trí của xâu x trong y")
           
        print(f'Dịch theo Max({bmBc[ord(y[j + m - 1])]}, {qsBc[ord(y[j + m])]})\n')
        j += max(bmBc[ord(y[j + m - 1])], qsBc[ord(y[j + m])])
 
x = 'GCAGAGAG'
y = 'GCATCGCAGAGAGTATACAGTACG'
n, m = len(y), len(x)
S(x, y, m, n)
