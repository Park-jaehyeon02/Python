#-*-coding:CP949-*-

"""
f = open("password.txt","r",encoding="utf8")
(r_id,r_pass) = tuple(f.readline().split(" "))
print("������ ������ ���������� ��ȸ�Ͽ����ϴ�.")
print(r_id,r_pass)
while True:
   m_id = input("���̵� �Է�: ")
   m_pass = input("��й�ȣ �Է�: ")
   if (m_id==r_id and m_pass ==r_pass):
       print("�α��ο� �����Ͽ����ϴ�.")
       break
   else:
       print("���̵� �Ǵ� ��й�ȣ�� �߸� �ԷµǾ����ϴ�.")
"""

"""
f = open("Goldensaying.txt","r",encoding="utf8")
li=[]
for i in f:
    i = i.rstrip('\n')
    li.append(i)
print("ù��° ���: ",li[0])
print("�ι�° ���: ",li[1])
m1_set = set(li[0].split(" "))
m2_set = set(li[1].split(" "))

print("ù��° ��� ����: ",m1_set)
print("�ι�° ��� ����: ",m2_set)
print("���� �ܾ�: ",m1_set.intersection(m2_set))
f.close()
"""

"""
f1 = open("sample1.txt","r",encoding="euc-kr")
f2 = open("sample2.txt","r",encoding="euc-kr")
li1=[]
li2=[]
count = [0,0]
print("="*4+" 1�� ���� "+"="*4)
for i in f1:
    i = i.rstrip()
    count[0] +=1
    count[1] +=len(i.split())
    for j in i.split():
        li1.append(j)
print("�� ������ ��:",count[0])
print("�� �ܾ��� ��:",count[1])

count = [0,0]
print("="*4+" 2�� ���� "+"="*4)
for i in f2:
    i = i.rstrip()
    count[0] +=1
    count[1] +=len(i.split())
    for j in i.split():
        li2.append(j)
print("�� ������ ��:",count[0])
print("�� �ܾ��� ��:",count[1])
set1=set(li1)
set2=set(li2)
print("="*5+" ���� �� "+"="*5)
inter = set1&set2
print("���� �ܾ��� ��:",len(inter))
print("���� �ܾ�: ",inter)
f1.close()
f2.close()
"""

"""
f= open("sample1.txt","r",encoding="euc-kr")
count =[0,0]
m_set = set()
for i in f:
    i = i.rstrip()
    i = i.split()
    count[0] +=1
    count[1] += len(i)
    for j in i:
       m_set.add(j)

print("�� ������ ��: ",count[0])
print("�� �ܾ��� ��: ",count[1])
print("�ߺ����� �ܾ��� ��: ",len(m_set))
print("�ߺ� �ܾ� ����: %0.2f%%"% ((count[1]-len(m_set))/count[1]*100))
f.close()
"""

