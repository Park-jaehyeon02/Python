# -*- coding: CP949 -*-
#�¿�����, �߷����� -> ???????
print(10**19)
print("���� ���� |{0:<20}|".format("��ü"))
print("���� ���� |{0:>20}|".format("��ü"))
print("�߾� ���� |{0:^20}|".format("��ü"))

print("���� ���� |{0:+^20}|".format("��ü"))
print("���� ���� |{0:=^20}|".format("��ü"))
print("���� ���� |{0:$^20}|".format("��ü"))

#F-string format
year = 2019
area = "�ƻ�"
print(f"���� {area}�� ����־��")

str = f"���� {area}�� ����־��"
print(str)

list = [10,20,30,40,50]
dict = {"name":"IU","area":"����"}
print(f'����Ʈ : {list[0]},{list[1]},{list[2]}')
#""�� ����� �� print�� ���ڿ��� �Ȱ�ġ�� ���� SyntaxError!
#ex) " dict['key'] " or ' dict["key"]'
print(f'�̸� : {dict["name"]}, ��°� :{dict["area"]}')