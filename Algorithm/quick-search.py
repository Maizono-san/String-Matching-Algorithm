def preQsBc(x):
    ASIZE = 256  # Assuming ASCII characters
    m = len(x)
    qsBc = [m+1] * ASIZE
    for i in range(m):
        qsBc[ord(x[i])] = m - i
    return qsBc
 
def search(x, y, m, n):
    qsBc = preQsBc(x)
   
    j = 0
    while j <= n - m:
        if x == y[j : j + m]:
            print(f"Vị trí {j} xuất hiện vị trí của xâu x trong y")
           
        print(f'Dịch {qsBc[ord(y[j + m])]}\n')
        j += qsBc[ord(y[j + m])]
 
x = 'GCAGAGAG'
y = 'GCATCGCAGAGAGTATACAGTACG'
n, m = len(y), len(x)
search(x, y, m, n)
