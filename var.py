# -*- coding: CP949 -*-
# -*- coding: "utf-8" -*-
"""
p = int(input("���ڸ� �Է��ϼ��� : "))
q = int(input("�и� �Է��ϼ��� : "))
print(p,"/",q,"�������� �� : ",p/q)
print(p,"/",q,"�������� �� : ",p//q) 
print(p,"/",q,"�������� ������ : ",p%q)

n = int(input("������ �Է��ϼ��� : "))
print(n%2)

n = int(input("�ʸ� �Է��ϼ��� : "))
m = n//60
s = n%60
print(m,"��",s,"��")


a = int(input("�Ƹ޸�ī�� �Ǹ� ���� :"))
c = int(input("ī��� �Ǹ� ���� :"))
ch = int(input("īǪġ�� �Ǹ� ���� :"))
print("�� ������ ",(a*2000+c*3000+ch*3500)//1000,",%03d" % ((a*2000+c*3000+ch*3500)%1000),"�Դϴ�.")

f-string!
����


f = int(input("ȭ���µ�: "))
c = (f-32)*5/9
print("�����µ�: ",c)


weight = float(input("�����Ը� kg ������ �Է��Ͻÿ� : "))
height = float(input("Ű�� ���� ������ �Է��Ͻÿ� : "))
bmi = weight/(height**2)
print("����� BMI=",bmi)

n = int(input("������ ��: "))
cost = int(input("���ǰ�: "))
print("�Ž�����: ",n-cost)
ch = n-cost

print("500�� ������ ����:",ch//500)
print("100�� ������ ����:",(ch%500)//100)
"""

a=1000
r=0.05
n=10

print(a*(1+r)**n)