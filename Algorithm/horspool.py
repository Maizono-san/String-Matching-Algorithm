def preBmBc(x):
    ASIZE = 256  # Assuming ASCII characters
    m = len(x)
    bmBc = [m] * ASIZE
    for i in range(m - 1):
        bmBc[ord(x[i])] = m - i - 1
    return bmBc
 
def HS(x, y, m, n):
    bmBc = preBmBc(x)
   
    j = 0
    while j <= n - m:
        if x == y[j : j + m]:
            print(f"Vị trí {j} xuất hiện vị trí của xâu x trong y")
           
        print(f'Dịch {bmBc[ord(y[j + m - 1])]}\n')
        j += bmBc[ord(y[j + m - 1])]
 
x = 'GCAGAGAG'
y = 'GCATCGCAGAGAGTATACAGTACG'
n, m = len(y), len(x)
HS(x, y, m, n)