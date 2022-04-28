#-*-coding:CP949-*-

"""
Heroes = []
Heroes.append("���̾��")
Heroes.append("���� ��Ʈ������")
print(Heroes)

letters = ["A","B","C","D","E","F"]
print(letters[-3:-1])
print(letters[0:])
print(letters[:])
print(letters[:-2])



Heroes = ["���̾��","�丣","��ũ","��Į�� ��ġ"]
Heroes[2] = "�����̴���"
Heroes.append("���۸�")
Heroes.insert(0,"��Ʈ��")
Heroes.insert(3,"�������")

Heroes.remove("��Į�� ��ġ")

#if "�丣" in Heroes:
#    Heroes.remove("�丣")


del Heroes[0]
print("del Heroes[0] :", Heroes)
Heroes.pop
print("Heroes.pop :", Heroes)
print("Heroes.index('���۸�') : ",Heroes.index("���۸�"))

print("each Hero!")
for hero in Heroes:
    print(hero)

Heroes.sort()
print("Heroes.sort() : ",Heroes)

Heroes.sort(reverse=True)
print("Heroes.sort(reverse=True) : ",Heroes)

new_heroes = sorted(Heroes)
print("new_heroes = sorted(Heroes) : ",new_heroes)

import random

sockdam = []
sockdam.append("��� ���� ���� �� �ִ� ���Ƿ� ������ ���� �ϳ��� ����.")
sockdam.append("���� �����. �׷��� ����� ������ �̱� �� �ִ�.")
sockdam.append("����� ����� �� ������ ������ �ȴ�")
print("#"*20)
print("# ������ �Ӵ� #")
print("#"*20)
print(random.choice(sockdam))

num = [[10,20,30,40,50,60]]
print(num)

num = [[10,20,30],[40,50,60]]
print(num)

print(num[0][0])
print(num[0][1])
print(num[1][1])
num[1][2] = 100
print(num)

he = []
for i in range(5):
    name = input("�������� �̸��� �Է��Ͻÿ�: ")
    he.append(name)

for i in he:
    print(i,end=" ")


phone_book = {"ȫ�浿" : "010-1234-5678"}
phone_book["������"] = "010-1234-5679"
phone_book["�̼���"] = "010-1234-5680"
print(phone_book)

print(phone_book["�̼���"])
print(phone_book.keys())
print(phone_book.values())

phone_book = {"ȫ�浿" : ["010-1234-5678",21]}
phone_book["������"] = ["010-1234-5679",24]
phone_book["�̼���"] = ["010-1234-5680",30]

print(phone_book["������"][1])


phone_book = {"ȫ�浿" : "010-1234-5678",
             "������" : "010-1234-5679",
             "�̼���" : "010-1234-5680"}

for key in sorted(phone_book.keys()):
    print(key,phone_book[key])

del phone_book["ȫ�浿"]
print(phone_book)

print(phone_book.pop('�̼���'))
print(phone_book)

phone_book = {"ȫ�浿" : "010-1234-5678",
             "������" : "010-1234-5679",
             "�̼���" : "010-1234-5680"}
phone_book.clear()
print(phone_book)

phone_book = {"ȫ�浿" : "010-1234-5678",
             "������" : "010-1234-5679",
             "�̼���" : "010-1234-5680"}
for i in phone_book.keys():
    print(i)
for i in phone_book.values():
    print(i)

for k,v in phone_book.items():
    print("{}�� ��ȭ��ȣ�� {}�Դϴ�.".format(k,v))

sales = {"�ݶ�" : "4","���̴�" : "5","�ﰢ���" : "10"}
print(sales[input("������ �̸��� �Է��Ͻÿ�: ")])

a = {"one":"�ϳ�","two":"��","three":"��"}
print(a[input("�ܾ �Է��Ͻÿ�: ")])
"""


"""
#�ǽ� ����

ins = {"����" : 2,"����":1,"��":0}
li = []
while(True):
    avg = 0
    g_ins = input("����� �Է��ϼ���: ")
    if 0==ins[g_ins]:
        break
    elif 1==ins[g_ins]:
        li.pop()
    elif 2==ins[g_ins]:
        li.append(int(input("�����͸� �Է��ϼ���: ")))
    for i in li:
        avg += i
    avg /= len(li)
    print(li,"avg:%0.2f" % avg)

s=[]
for i in range(5):
    s.append(int(input("������ �Է��ϼ���:")))
print(s)
n_sum =0
cnt = 0
n_max = s[0]
n_min = s[0]
for i in s:
    n_sum += i
    if i>n_max:
        n_max = i
    if i<n_min:
        n_min = i
    if i>=90:
        cnt+=1
print("���:%0.2f" % (n_sum/len(s)))
print("�ְ� ����:%d" % n_max)
print("���� ����:%d" % n_min)
print("90�� �̻� �л�:%d��" % cnt)


data = []
for i in range(3):
    line=[]
    for j in range(2):
        line.append((i*10)+j)
    data.append(line)

print(data)


li = []
for i in range(5):
    hak = input("�й�: ")
    name = input("�̸�: ")
    korean = int(input("����: "))
    english =  int(input("����: "))
    math = int(input("����: "))
    li.append([hak,name,korean,english,math,korean+english+math])

print(li)
print("="*5+"�̸��� ����"+"="*5)

li2=[]
for i in li:
    li2.append(i[1])
li2.sort()

li3=[]
for i in li2:
    for j in li:
        if li2[0]==j[1]:
            li3.append(j)
    del li2[0]
for i in li:
    if li2[0]==i[1]:
        li3.append(i)
print(li3)
print("="*5+"������ ����"+"="*5)
li2=[]
for i in li:
    li2.append(i[5])
li2.sort()
li2.reverse()
li3=[]
for i in li2:
    for j in li:
        if li2[0]==j[5]:
            li3.append(j)
    del li2[0]
for i in li:
    if li2[0]==i[5]:
        li3.append(i)
print(li3)
"""

"""
sorted(list , key=lambda x: x[1]) 1�� �Τ��ؽ����� �������� ������������ ����

sorted(list , key=lambda x: -x[5]) ������������ ����
"""

"""
li=[]
for i in range(3):
    tli=[]
    for j in range(3):
        tli.append(int(input("�����͸� �Է��ϼ���: ")))
    nsum = 0
    for j in tli:
        nsum+=j
    tli.append(nsum)
    li.append(tli)

for i in li:
    print("-"*10)
    print(i[0],i[1],i[2],i[3])
tsum=0
print("-"*10)
for i in range(3):
    nsum=0
    for j in range(3):
        nsum+=li[j][i]
    print(nsum,end=" ")
    tsum+=nsum
print(tsum)

print("-"*10)
"""

d = {'a':"����","d":"����","s":"�˻�","p":"���","e":"����"}
li = []
while(True):
    ins = input("����� �Է��ϼ���: ")
    if d[ins] =="����":
       li.append(input("�̸��� �Է��ϼ���: "),input("��ȭ��ȣ�� �Է��ϼ���: "))
    if d[ins] =="����":
        tmp = input("�̸��� �Է��ϼ���: ")
        if tmp in li:
            for i in range(len(li)):
                if li[i][0]==tmp:
                    del li[i]
        else:
            print(tmp,"�������� ����!!")
    if d[ins] =="�˻�":
        tmp = input("�̸��� �Է��ϼ���: ")
        if tmp in li:
           for i in range(len(li)):
                if li[i][0]==tmp:
                    print(li[i])

        else:
            print(tmp,"�������� ����!!")
    
    if d[ins] =="���":
        
    if d[ins] =="����":
         print("���α׷�����!!")
         break

"""
get �Լ�
"""