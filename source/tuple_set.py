#-*-coding:CP949-*-

"""
t = ()
t2 = (1,) #1�� ���鶧�� �ĸ��� ����� �Ծ��ϸ� ������ �Ҵ��
i = (1)
t3 = (1,2,3,4)
t4 = 1,2,3,4
li = [1,2,3,4]
t5 = tuple(li)
t6 = t3+t4 #���ϱ� ������ ������
print(t,t2,t3,t4,t5,i)
print(type(i))
"""
"""
student = ("ö��",19,"CS")
(name,age,major) = student
print(name,"\n",age,"\n",major)
t = (10,20,30,40,50,60,10,20,60,10)
print(t.count(10))
print(t.index(60))
"""
"""
r = float(input("���� �������� �Է��Ͻÿ�: "))
cir = (3.)
"""

"""
print("������ ���� ���� ���α׷��Դϴ�.")
account = []
account.append(input("������ ���̵� �Է�: "))
account.append(input("������ ��й�ȣ �Է�: "))
while(True):
    account.append(input("������ ���̵� �Է�: "))
    if account[1]==account[2]:
        print("������ ���������� �����Ǿ����ϴ�.")
        break
    else:
        del account[2]
        print("��й�ȣ�� ���� �ٸ��ϴ�.")
t_a = tuple(account)
print(t_a)
"""

"""
#��Ʈ(set)
numbers = {2,1,3}
print(numbers)
print(len(numbers))
fruits = {"apple","banana"}
# ��Ʈ�� �ε��� ������ �Ұ�����
numbers.add(4)
print(numbers)
numbers.discard(2)
print(numbers)
numbers.remove(1)
print(numbers)
numbers.clear()
print(numbers)
"""

"""
add
discard
clear
union ������
difference ������
intersection ������
symetric_difference ��Ī ������
issubset �κ�����
"""

"""
s1 = {1,3,5,7}
s2 = {2,4,7,9}
union = s1.union(s2) # s1 | s2
print("s1 | s2 =",union)
intersec = s1.intersection(s2) # s1& s2
print("s1 & s2 =",intersec)
diff = s1 -s2 
print("s1 - s2=",diff)
dym_diff = s1 ^ s2 #s1.dsymmetric_difference(s2)
print("s1 ^ s2 =",dym_diff)
"""

"""
s1 = {1,3,5,7,8}
s2 = {2,4,7,8,9}
s3 = {5,6,8,10}
union = s1 | s2 | s3
print(union)
intersec = s1 & s2 & s3
print(intersec)
diff = s1 -s2 - s3
print(diff)
dym_diff = s1 ^ s2 ^ s3
print(dym_diff) # �� 8�� ��µǴ��� ������ ����
"""

"""
s1= {1,3,5,7,8}
s2 = {2,4,7,8,}
s3 = {5,8}
s4 = {6,9}
sub_set = s2.issubset(s1) # s2�� s1�� �Ӻκ�����
print(sub_set)
sub_set = s3.issubset(s1) # s3�� s1�� �Ӻκ�����
print(sub_set)
sup_set = s1.issuperset(s2) # ��������
print(sup_set)
sup_set = s1.issuperset(s3) # ��������
print(sup_set)
dis_join = s1.isdisjoint(s2) # ���μ�
print(dis_join)
dis_join = s1.isdisjoint(s2) # ���μ�
print(dis_join)
"""

"""
a = {"ȫ�浿","�̼���","������","������"}
b = {"�̼���","������","������"}
print(a&b)
"""

"""
s1 = "hello everyone"
s2= "Have a great day!!"
li = list(set(s1)&set(s2))
print(li)
"""
s1 = "�����̰� �ĵ帮�� ���ϼ��� ���� ù Ȩ���� �Ͷ߷ȴ�. ���ϼ��� 21��(�ѱ��ð�) �̱� Ķ�����Ͼ��� �����̰� ���� ��ũ���� ���� �Žó�Ƽ ������� ��⿡�� 9�� 3����� ���������ߴ�."
se = set(s1.split(" "))
print("���� �ܾ��:",len(s1.split(" ")))
print(se)
