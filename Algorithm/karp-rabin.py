import sys

q = sys.maxsize

def rehash(a,b,h):
    return (((h - a*d) << 1) + b) % q

def KR(x,m,y,n):
    hx, hy, j = 0, 0, 0
    for i in range(m):
        hx = ((hx << 1) + ord(x[i])) % q
        hy = ((hy << 1) + ord(y[i])) % q
    while j <= n - m:
        # print(f"Lần thử {j + 1}")
        # print(hx)
        # print(hy)
        if hx == hy and x == y[j:m+j]:
            print(f"Vị trí {j} xuất hiện vị trí của xâu x trong y")
        if j < n - m:
            hy = rehash(ord(y[j]), ord(y[j+m]),hy) 
        j += 1

x = 'GCAGAGAG'
y = 'GCATCGCAGAGAGTATACAGTACG'
m = len(x)
n = len(y)
d = 1 
for i in range(1,m):
    d = d << 1

KR(x,m,y,n)


