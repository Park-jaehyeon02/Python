#-*-coding:CP949-*-

import math

def mersennes(n):
    prime = []
    t = 2
    for i in range(2,n):
        candidate = (2**t)-1
        t += 1
        if candidate > n: break
        prime.append(candidate)
    
    for j in prime:
        for k in range(2,int(math.sqrt(j))+1):
            if (j%k) ==0:
                prime.remove(j)
                break
    return print(prime)

mersennes(10000)