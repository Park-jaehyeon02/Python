# -*-coding:CP949-*-

"""
���� ������
compound operator



x= 1000
print("�ʱⰪ x=",x)
x += 2
print("x += 2 :",x)
x -= 2
print("x -= 2 :",x)


#�켱 ������ ����
x = int(input("ù ��° ���� �Է��Ͻÿ� :"))
y = int(input("�� ��° ���� �Է��Ͻÿ� :"))
z = int(input("�� ��° ���� �Է��Ͻÿ� :"))
avg = (x + y + z) /3
print("��� : ",avg)


#���� ������
a,b = 100,200
print(a==b,a !=b,a>b,a<b,a>=b,a<=b)

a = 99
print((a>100) and (a<200))
print((a>100) or (a<200))
print(not(a==100))


#bit ���� & ->bit������ and
print(10 & 7)
print(123 & 456)
print(0xffff & 0x00000)

#bit ���� | -> bit������ or
print(10 | 7)
print(123 | 456)
print(0xffff | 0x0000)

#��Ʈ ��Ÿ�� ���� ^ ������ 
print(10 ^ 7)
print(123 ^ 456)
print(0xffff ^ 0x0000)

#bit ���� ������ ~
a =12345
~a + 1
print(a)
#? -12345 �ȳ���

#���� ����Ʈ ������ <<
#2bit ����Ʈ �ϸ� �պ�Ʈ 2���� ������� �ڿ� 00�� ������
#n����Ʈ �ϸ� 2^n�� ���ϴ� ȿ���� ��
a = 10
print(a<<1,a<<2,a<<3,a<<4)

"""
#������ ����Ʈ ������ >>
#2^n���� ������ ȿ���� ��Ÿ��
#�� ���� ȿ���� ��Ÿ��

a = 10
print(a>>1,a>>2,a>>3,a>>4)
"""