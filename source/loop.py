#-*-coding:CP949-*-

"""
s= 1
n = int(input("������ �Է��Ͻÿ�: "))
for i in range(n):
    s*=i+1
print(n,"\b!�� ",s,"\b�̴�")
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