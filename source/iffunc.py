#-*-coding:CP949-*-

"""
n = int(input("������ �Է��ϼ���:"))

if n%4==0 and n%100 != 0 or n%400==0:
    print("{0}���� �����Դϴ�.".format(n))
else:
    print("{0}���� ������ �ƴմϴ�.".format(n))

"""

"""
import random

n = random.randrange(2)
print("���� ������ ������ �����մϴ�.")

if n==0:
    print("�޸��Դϴ�.")
else:
    print("�ո��Դϴ�.")

print("������ ����Ǿ����ϴ�.")
"""

"""
import random
time =  random.randint(1,24)
sunny = random.choice([True,False])

print("���� ��ħ�Դϴ�. ���� �ð��� ",time,"���Դϴ�.")
"""

"""
import random
a = int(input("��a�� ����: "))
b = int(input("��b�� ����: "))
c = int(input("��c�� ����: "))

if (c**2==a**2+b**2):
    print("�����ﰢ���Դϴ�.")
else:
    print("�����ﰢ���� �ƴմϴ�.")

"""

"""
h = float(input("����� Ű��? : "))
g = input("����� ������? ���� or ���� : ")

if (g=="����"):
    if (h>=173.5):
        print("����� ���Ű �̻��Դϴ�.")
    else:
        print("����� ���Ű �̸��Դϴ�.")
else:
    if (h>=163.2):
        print("����� ���Ű �̻��Դϴ�.")
    else:
        print("����� ���Ű �̸��Դϴ�.")

"""

"""
n = int(input("������ �Է��ϼ��� : "))

print("20��",end='')
if (n%4==0):
    print("4�� ����Դϴ�.")
elif (n%5==0):
    print("5�� ����Դϴ�.")
elif (n%4==0 and n%5==0):
    print("4�� ����̸鼭 5�� ����Դϴ�.")
else:
    print("4, 5 �Ѵ��� ����� �ƴմϴ�.")
"""

"""
a = int(input("���̸� �Է��ϼ��� : "))
h = float(input("Ű�� �Է��ϼ��� : "))

if (a>=10 and h>=165):
    print("���̱ⱸ�� �̿��Ҽ� �ֽ��ϴ�.")
else:
    if(a<10 and h<165):
        print("{}���̰� {}cm Ű�� ���̱ⱸ�� �̿��ϽǼ� �����ϴ�.".format(a,h))
    elif (a<10):
        print("{}���� ���̱ⱸ�� �̿��ϽǼ� �����ϴ�.".format(a))
    else:
        print("{}cm Ű�� ���̱ⱸ�� �̿��ϽǼ� �����ϴ�.".format(h))
"""

"""
import datetime as dt
d = dt.datetime.now()

d_dic={0:"������",1:"ȭ����",2:"������",3:"�����",4:"�ݿ���",5:"�����",6:"�Ͽ���"}
print("������ {}�� {}�� {}�� {}".format(d.year, d.month, d.day, d_dic[d.weekday()]),end='')
if (d.time().hour>=12):
    print("���� ",end='')
    if(d.time().hour==12):
        print("{}�� {}�� �Դϴ�.".format(d.time().hour, d.time().min))
    else:
        print("{}�� {}�� �Դϴ�.".format(d.time().hour-12, d.time().minute))
"""

s1 = int(input("���̽� ������ �Է��ϼ���: "))
s2 = int(input("C��� ������ �Է��ϼ���: "))
s3 = int(input("��ǻ�Ͱ��� ������ �Է��ϼ���: "))

t = s1+s2+s3
a = t/3

print("����: ",t)
print("���: %0.2f"%a)

if (a>=90):
    print("A���� �Դϴ�")
    print("������� ���л��Դϴ�.")
elif (a>=80):
    print("B���� �Դϴ�")
    print("����� �����Դϴ�.")
elif (a>=70):
    print("C���� �Դϴ�")
    print("���ݴ� ����ؾ� �մϴ�.")
elif (a>=60):
    print("D���� �Դϴ�")
    print("������ ����ؾ� �մϴ�.")
else:
    print("F���� �Դϴ�")
    print("������ ����� �ؾ��մϴ�")
