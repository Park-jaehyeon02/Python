#-*-coding:CP949-*-

"""
s= 1
n = int(input("정수를 입력하시오: "))
for i in range(n):
    s*=i+1
print(n,"\b!은 ",s,"\b이다")
"""

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
"""

"""
n = int(input("1부터 어느수까지의 홀수만 더하시겠습니까?: "))
s=0
for i in range(1,n+1,2):
    s+=i
print(s)
"""

"""
n=int(input("몇명의 장군을 입력하시겠습니까?: "))
name=[]

for i in range(n):
    name.append(input("장구느이 이름을 입력하세요: "))

for i in range(n):
    print("{}: {} 장군님 반갑습니다.".format(i+1,name[i]))
"""

"""
print(("="*30)+" 구구단 출력 "+("="*30))
print(end="  ")
for i in range(8):
    print(i+2,"단",end='   ')

print()

for i in range(8):
    for j in range(8):
        print("{0:1d}x{1:1d}={2:2d}".format(j+2,i+2,(j+2)*(i+2)),end=" ")
    print()
    """
    
"""
n  = int(input("다이아몬드의 크기(홀수): "))
for i in range(int((n+1)/2)):
    for j in range(int((n+1)/2)-(i+1)):
        print(" ",end="")
    for j in range(1+2*(i)):
        print("*",end="")
    print()

k = int((n+1)/2-1) 
for i in range(k):
    for j in range(i+1):
        print(" ",end="")
    for j in range(1+2*(int((n+1)/2)-1)-2*(i+1)):
        print("*",end="")
    print()
"""

"""
n = int(input("팩토리얼 계산을 원하는 값 입력: "))
p = 1
c = 1
while(c<=n):
    p *=c
    c+=1
print("{}! = {}".format(n,p))
"""

"""
n = input("이진수 입력: ")
count=0
Msum=0
while(len(n)>count):
    if(n[-(count+1)]=="1"):
        Msum += 2**count
    count += 1
   
print("10진수:",Msum)
print("10진수:%d" % int(n,2))
"""

"""
import random
ans = random.randint(1,101)
count = 1
while(True):
    q = int(input("숫자를 입력하시오: "))
    if(q==ans):
        print("{}시도 만에 정답을 맞추셨습니다.".format(count))
        break
    elif(q<ans):
        print("높다")
    else:
        print("낮다")
    count+=1
    if(count==11):
        print("기회끝")
        break
"""

