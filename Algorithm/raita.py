def preBmBc(x):
    ASIZE = 256  # Assuming ASCII characters
    m = len(x)
    bmBc = [m] * ASIZE
    for i in range(m - 1):
        bmBc[ord(x[i])] = m - i - 1
    return bmBc
 
def R(x, y, m, n):
    bmBc = preBmBc(x)
    firstC = x[0]
    middleC = x[m // 2]
    lastC = x[m - 1]
   
    j = 0
    while j <= n - m:
        c = y[j + m - 1]
        if y[j + m - 1] == lastC and y[j] == firstC and y[j + m // 2] == middleC:
            if x[1 : m - 1] == y[j + 1 : j + m - 1]:
                print(f"Vị trí {j} xuất hiện vị trí của xâu x trong y")
           
        print(f'Dịch {bmBc[ord(c)]}\n')
        j += bmBc[ord(c)]
 
x = 'GCAGAGAG'
y = 'GCATCGCAGAGAGTATACAGTACG'
n, m = len(y), len(x)
R(x, y, m, n)