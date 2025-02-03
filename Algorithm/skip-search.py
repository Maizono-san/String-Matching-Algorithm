def build_z_table(x):
    ASIZE = 256  # Assuming ASCII characters
    m = len(x)
    z = [[] for _ in range(ASIZE)]
    for i in range(m-1, -1, -1):
        z[ord(x[i])].append(i)
   
    return z
       
def search(x, y, m, n):
    z = build_z_table(x)
   
    for j in range(m-1, n, m):
        print(f'Ở vị trí {j}')
        print(f'y = {y[j - m + 1 : j + 1]}')
        print(f'x = {x}')
        for node in z[ord(y[j])]:
            print(f'+ p = {j} - {node} = {j - node}')
            print(f'y = {y[j - node : j - node + m]}')
            print(f'x = {x}')
            if x == y[j - node : j - node + m]:
                print(f"Vị trí {j - node} xuất hiện vị trí của xâu x trong y")
        print()
 
x = 'GCAGAGAG'
y = 'GCATCGCAGAGAGTATACAGTACG'
n, m = len(y), len(x)
search(x, y, m, n)
