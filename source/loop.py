#-*-coding:CP949-*-

"""
s= 1
n = int(input("������ �Է��Ͻÿ�: "))
for i in range(n):
    s*=i+1
print(n,"\b!�� ",s,"\b�̴�")
"""

"""
import random
ans = random.randint(1,101)
c = 0
print("1����100������ ���ڸ� ���߽ÿ�")
while True:
    q = int(input("���ڸ� �Է��Ͻÿ�: "))

    if(ans == q):
        print("�����մϴ�. �õ�Ƚ��:",c)
        break
    elif(ans>q):
        print("����")
    else:
        print("����")
    c+=1
"""

"""
n = int(input("1���� ����������� Ȧ���� ���Ͻðڽ��ϱ�?: "))
s=0
for i in range(1,n+1,2):
    s+=i
print(s)
"""

"""
n=int(input("����� �屺�� �Է��Ͻðڽ��ϱ�?: "))
name=[]

for i in range(n):
    name.append(input("�屸���� �̸��� �Է��ϼ���: "))

for i in range(n):
    print("{}: {} �屺�� �ݰ����ϴ�.".format(i+1,name[i]))
"""

"""
print(("="*30)+" ������ ��� "+("="*30))
print(end="  ")
for i in range(8):
    print(i+2,"��",end='   ')

print()

for i in range(8):
    for j in range(8):
        print("{0:1d}x{1:1d}={2:2d}".format(j+2,i+2,(j+2)*(i+2)),end=" ")
    print()
    """
    
"""
n  = int(input("���̾Ƹ���� ũ��(Ȧ��): "))
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
n = int(input("���丮�� ����� ���ϴ� �� �Է�: "))
p = 1
c = 1
while(c<=n):
    p *=c
    c+=1
print("{}! = {}".format(n,p))
"""

"""
n = input("������ �Է�: ")
count=0
Msum=0
while(len(n)>count):
    if(n[-(count+1)]=="1"):
        Msum += 2**count
    count += 1
   
print("10����:",Msum)
print("10����:%d" % int(n,2))
"""

"""
import random
ans = random.randint(1,101)
count = 1
while(True):
    q = int(input("���ڸ� �Է��Ͻÿ�: "))
    if(q==ans):
        print("{}�õ� ���� ������ ���߼̽��ϴ�.".format(count))
        break
    elif(q<ans):
        print("����")
    else:
        print("����")
    count+=1
    if(count==11):
        print("��ȸ��")
        break
"""

