def preBmBc(x):
    ASIZE = 256  # Assuming ASCII characters
    m = len(x)
    bmBc = [m] * ASIZE
    for i in range(m - 1):
        bmBc[ord(x[i])] = m - i - 1
    return bmBc
 
def TBM(x, y, m, n):
    bmBc = preBmBc(x)
    shift = bmBc[ord(x[m - 1])]
    bmBc[ord(x[m - 1])] = 0
    y += x[m - 1] * m
   
    j = 0
    while j <= n-m:
        print(f'index bắt đầu {j}, bắt đầu với y = {y[j : j + m]}')
        k = bmBc[ord(y[j + m -1])]
        if k == 0:
            print(f'Dịch 0, y = {y[j : j + m]}')
        while k !=  0:
            j += k
            print(f'Dịch {k}, y = {y[j : j + m]}')
            k = bmBc[ord(y[j + m -1])]
           
            j += k
            print(f'Dịch {k}, y = {y[j : j + m]}')
            k = bmBc[ord(y[j + m -1])]
           
            j += k
            print(f'Dịch {k}, y = {y[j : j + m]}')
            k = bmBc[ord(y[j + m -1])]
           
        if x[ : m - 1] == y[j : j + m - 1]:
            print(f"Vị trí {j} xuất hiện vị trí của xâu x trong y")
        j += shift
        print(f'Lần dịch cuối {shift}')
        print()
 
x = 'GCAGAGAG'
y = 'GCATCGCAGAGAGTATACAGTACG'
n, m = len(y), len(x)
TBM(x, y, m, n)