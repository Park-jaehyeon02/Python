#-*-coding:CP949-*-

"""
n1 =123
n2 = -123
n3 = 0
n4 =3.14
n5 = -3.14
n6 = 0.0
print(type(n1),type(n2),
type(n3),
type(n4),
type(n5),
type(n6))
"""

"""
complex j�� ��� i�� ����ؼ� ǥ����
n1= 10+30j
print(type(n1))
"""

"""
print("'test'")
print('"test"')
print("���� ����"+str(21)+"���̴�.")
"""

"""
s = 'abcdefghijklmn'
for i in range(len(s)):
    print(s[i])
for i in range(len(s)):
    print(i)

print(s[0:2])
#0���� 5�̸� ���� 2���� �� ���
print(s[0:6:2])
"""
"""
name = input("�ȳ��ϼ��� �̸��� ��� �ǽó���? ")
print("�ݰ����ϴ� %s ��" % name)
print("�̸��� ���̴� ������ ������: ",len(name))
age = int(input("���̰� ��� �ǳ���?: "))
print("�����̸� ",age+1,"�� �ǽô±���")
"""

"""
print("�����ٶ�",end='')
print("���ٻ�")
"""
"""
year = int(input("������ ������ �Է��Ͻÿ�: "))
month = int(input("������ ���� �Է��Ͻÿ�: "))
day= int(input("������ �ϸ� �Է��Ͻÿ�: "))

print("������ ",year,"��",month,"��",day,"���Դϴ�.")
"""

"""
import time
now = time.time()
year = int(1970 +now//(365*24*3600))
print("���ش�",year,"�Դϴ�.")
age = int(input("�� ���̽Ű���? "))
print("2050�⿡��",age+2050-year,"�� �̽ñ���.")
"""

"""
print("�ұݹ��� �󵵸� ���ϴ� ���α׷��Դϴ�")
gram = int(input("�ұ��� ���� �� g�Դϱ�?" ))
water = int(input("���� ���� �� g�Դϱ�?" ))
print("�ұݹ��� ��: %0.2f %%" % (gram/(water+gram)*100))
"""

"""
list = []
for i in range(5):
    list.append(input("ģ���� �̸��� �Է��Ͻÿ�: "))
print(list)
"""

"""
list = []
list.append(input("�̸���? "))
list.append(int(input("��ȭ��ȣ��? ")))
list.append(int(input("���̴�? ")))

print(list)
"""

"""
c_num1 = 2.7 + 3.2j
c_num2 = 5.1 + -2.6j
print("���� ���: %0.2f + %0.2fi "%( c_num1.real+c_num2.real,c_num1.imag+c_num2.imag))
print("���� ���: %0.2f + %0.2fi "%( c_num1.real-c_num2.real,c_num1.imag-c_num2.imag))
print("���� ���: %0.2f + %0.2fi "%( c_num1.real*c_num2.real,c_num1.imag*c_num2.imag))
print("%0.1f + %0.1fi ���Ҽ��� �Ǽ��κ� : %0.2f"%(c_num1.real,c_num1.imag,c_num1.real))
print("%0.1f + %0.1fi ���Ҽ��� �Ǽ��κ� : %0.2f"%(c_num1.real,c_num1.imag,c_num1.imag))

print("%0.1f + %0.1fi ���Ҽ��� �ӷ����Ҽ� : %0.2f + %0.2fj"%(c_num2.real,c_num2.imag,c_num2.conjugate().real,c_num2.conjugate().imag))
print("%0.1f + %0.1fi ���Ҽ��� ũ�� : %0.5f"%(c_num2.real,c_num2.imag,abs(c_num2)))

"""

"""
import datetime as dt

dt_now = dt.datetime.now()
print(dt_now)
print("������ {0}�� {1}�� {2}�� �Դϴ�.".format(dt_now.year,dt_now.month,dt_now.day))
print("���� �ð��� {0}�� {1}�� �Դϴ�.".format(dt_now.hour,dt_now.minute))
print("�ѱ��� ǥ��(��/��/��): {0:04d}/{1:02d}/{2:02d}".format(dt_now.year,dt_now.month,dt_now.day))
print("�̱��� ǥ��(��/��/��): {1:02d}/{2:02d}/{0:04d}".format(dt_now.year,dt_now.month,dt_now.day))
print("������ ǥ��(��/��/��): {2:02d}/{1:02d}/{0:04d}".format(dt_now.year,dt_now.month,dt_now.day))
"""

"""
import datetime as dt

td = dt.datetime.today()
print("������ {0}�� {1:02d}�� {2:02}�� �Դϴ�.".format(td.year,td.month,td.day))
d_d = td+dt.timedelta(days=100)
print("100�� �Ĵ� {0}�� {1:02d}��{2:02d}�� �Դϴ�.".format(d_d.year,d_d.month,d_d.day))

"""

"""
import datetime as dt

year = int(input("����⵵�� �Է��ϼ���: "))
month = int(input("������� �Է��ϼ���: "))
day = int(input("������� �Է��ϼ���: "))
print("�����({0}��{1}��{2}��)�� ���� {3},{4}�� �������ϴ�.".format(year, month, day, (dt.datetime.today() - dt.datetime(year,month,day)).days//1000,(dt.datetime.today() - dt.datetime(year,month,day)).days%1000 ))
"""

"""
import datetime as dt

n = int(input("���÷� ���� �����ĸ� �˰� �����Ű���? "))
p_d = dt.datetime.today() + dt.timedelta(days=n)
print("������ {0}��{1}��{2}�� �Դϴ�.".format(dt.datetime.today().year,dt.datetime.today().month,dt.datetime.today().day))
print("{3}���Ĵ� {0}��{1}��{2}�� �Դϴ�.".format(p_d.year,p_d.month,p_d.day,n))
"""

"""
import datetime as dt
p = []
p.append(input("����� �̸���? "))
p.append(int(input("����� ���̴�? ")))
p.append(float(input("����� Ű��? ")))
print(p)
print("�ȳ��ϼ��� ",p[0])
print("2050�⿡�� {}���� �ǽðڳ׿�".format(p[1]+2050-dt.datetime.today().year))
print("���� ���Ű�� 175.5cm�� {0:0.1f}cm, ���� ���Ű�� 163.2cm�� {1:0.1f}cm���̰� ���׿�.".format(p[2]-175.5,p[2]-163.2))
"""

li = []
su = 0
avg = 0.0
for i in range(5):
    li.append(int(input("������ �Է��Ͻÿ�:")))
    su += li[i]
avg = su/5
print(li)
print("������ �հ�: ",su)
print("������ ���: %0.2f"% avg)