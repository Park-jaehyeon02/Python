
# -*- coding: CP949 -*-

#format ����


year = 2022
month = 3 
day = 15
day_week = "ȭ"
temp = 15.3
a
print("{y}��{m}��{d}��{dw}�����Դϴ�.".format(m=month,d=day,dw=day_week,y=year))
print("{0:02d}��{1}��{2}������ �µ��� {3:.2f}���Դϴ�.".format(month,day,day_week,temp))


print("�ѱ��� ǥ�� (��/��/��/����) : {0}/{1}/{2}/{3}".format(year,month,day,day_week))
print("�̱��� ǥ�� (����/��/��/��) : {3}/{1}/{2}/{0}".format(year,month,day,day_week))
print("������ ǥ�� (����/��/��/��) : {3}/{2}/{1}/{0}".format(year,month,day,day_week))
""" 

# ���� ����
"""
number = 12345
print("��¿���:\b",10**9)
print("��������:{0:*<10}".format(number))

print("�߾�����:{0:0^10}".format(number))

print("��������:{0:=>10}".format(number))


n = "*****"
print("{0:>7}".format(n))
print("{0:^7}".format(n))
print("{0:<7}".format(n))

temp_str = "*"*5
print(temp_str)