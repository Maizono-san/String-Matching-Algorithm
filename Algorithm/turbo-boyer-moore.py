def preBmBc(x):
    ASIZE = 256  # Assuming ASCII characters
    m = len(x)
    bmBc = [m] * ASIZE
    for i in range(m - 1):
        bmBc[ord(x[i])] = m - i - 1
    return bmBc
 
def preBmGs(x):
    m = len(x)
    period_of_x = ''
    bmGs = [0] * (m + 1)
   
    # first element is the length of the period of x and will be removed when we returning the bmGs table
    bmGs[0] = len(period_of_x)
   
    # Helper function to check Cs condition
    def Cs(i, s):
        for k in range(i + 1, m):
            if s >= k or x[k - s] == x[k]:
                continue
            else:
                return False
        return True
   
    # Helper function to check Co condition
    def Co(i, s):
        if s >= i:
            return True
           
        if x[i - s] != x[i]:
            return True
        return False
   
    # Calculate bmGs
    for i in range(m):
        for s in range(1, m + 1):
            if Cs(i, s) and Co(i, s):
                bmGs[i + 1] = s
                break
   
    return bmGs[1:]
 
def TBM(x, y, m, n):
    j = u = 0
    shift = m
    bmGs = preBmGs(x)
    bmBc = preBmBc(x)
 
    while j <= n - m:
        i = m - 1
 
        while i >= 0 and x[i] == y[i + j]:
            i -= 1
            if u != 0 and i == m - 1 - shift:
                i -= u
 
        if i < 0:
            print(f"Vị trí {j} xuất hiện vị trí của xâu x trong y")
            shift = bmGs[0]
            u = m - shift
        else:
            v = m - 1 - i
            turboShift = u - v
            bcShift = bmBc[ord(y[i + j])] - m + 1 + i
            shift = max(turboShift, bcShift, bmGs[i])
            if shift == bmGs[i]:
                u = min(m - shift, v)
            else:
                if turboShift < bcShift:
                    shift = max(shift, u + 1)
                u = 0
 
        j += shift
       
x = 'GCAGAGAG'
y = 'GCATCGCAGAGAGTATACAGTACG'
m = len(x)
n = len(y)
TBM(x, y, m, n)