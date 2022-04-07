#-*-coding:CP949-*-

"""
s= 1
n = int(input("정수를 입력하시오: "))
for i in range(n):
    s*=i+1
print(n,"\b!은 ",s,"\b이다")
"""

import random
ans = random.randint(1,101)
c = 0
print("1부터100사이의 숫자를 맞추시오")
while True:
    q = int(input("숫자를 입력하시오: "))

    if(ans == q):
        print("축하합니다. 시도횟수:",c)
        break
    elif(ans>q):
        print("낮음")
    else:
        print("높음")
    c+=1