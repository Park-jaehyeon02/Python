#-*-coding:CP949-*-

"""
r = float(input("�������� �Է��ϼ���: "))
v = 4/3 * 3.141592 * r**3
print("���� ���� = %0.3f" %(v))
"""

"""

x = int(input("x�� ���� �Է��ϼ���: "))
y = 2*x**3 + 3*x**2 + 7*x +10
print("2*",x,"^3 + 3*",x,"^2 + 7*",x,"+10 = ",y)

format �������� �ۼ��ϸ� �� ����ϰ� ���ð� ������
x = int(input("x�� ���� �Է��ϼ���: "))
y = 2*x**3 + 3*x**2 + 7*x +10
print("2*{0}^3+3*{0}^2+7*{0}+10 = {1}".format(x,y))
�� ����� ��?
"""

"""
y = int(input("���� ��� ����� �Է��ϼ���:"))
r = float(input("���� �ݸ�(%)�� �Է��ϼ���:"))
o = int(input("���� ������ �Է��ϼ���:"))
re = o * ( (1 + r/100) ** y)
print("�� ���� �ݾ�: %d��" % re)
"""

"""
put = int(input("����� ��ȯ�� ���� �Է��ϼ���: "))
five = put//50000
put %= 50000
ttho = put//10000
put %= 10000
ftho = put//5000
put %= 5000
tho = put//1000
put %= 1000
print("5���� ����:%d��"% five)
print("1���� ����:%d��"% ttho)
print("5õ�� ����:%d��"% ftho)
print("1õ�� ����:%d��"% tho)
print("������ �ܵ�: %d��" % put)
"""

"""
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

val = 2*(x**3)+ 3*(x**2)*(y**2) + 7*x*(z**3) - 5*y
val2 = (x+y)/(2*x*z)
print("2*{0}^3+3*{0}^2*{1}^2+7*{0}*{2}^3-5*{1} = {3:0.2f}".format(x,y,z,val))
print("{0} + {1} / 2*{0}*{1} = {2:0.2f}".format(x,z,val2))
"""

"""
x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))
r = ((x2-x1)**2 + (y2-y1)**2))**0.5
print("�� �� ������ �Ÿ�:%.2f" % r)
"""



x = int(input("x: "))
y = int(input("y: "))

print("x:",bin(x))
print("y:",bin(y))
print("&: ",bin(x&y),"=>",x&y)
print("|: ",bin(x|y),"=>",x|y)
print("^: ",bin(x^y),"=>",x^y)
