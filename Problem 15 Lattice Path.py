import time
 
def route_num(size):
    L = [1] * size #make a list contains cube dot
    for i in range(size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[size - 1]
 
start = time.time()
n = route_num(20)
elapsed = (time.time() - start)
print(n,elapsed)
