#-*-coding:CP949-*-

"""
#���� ó��
try:
    1/0
except ZeroDivisionError:
    print("0���� ������ ����")

try:
    1/0
except Exception as e:
    print(e)
"""

#���� ���� ó��
"""
try:
    5/3
except ZeroDivisionError:
    print("0���� ����")
except IOError:
    print("����� ����")
else:
    print("���� ����")
finally:
    print("���� ��� ���� �����")
"""

"""
f = open("data.txt","r",encoding="utf8")
cnt = 0
to = 0
for i in f:
    i = i.split()
    cnt += len(i)
    for j in i:
        to += int(j)
        if int(j)%2==0:
            print("%s: ¦��"%j)
        else:
            print("%s: Ȧ��"%j)
print("������ ����: %d"% cnt)
print("������ ����: %d"% to)
print("������ ����: %.2f"% to/cnt)
f.close()
"""

"""
f = open("text.txt","r",encoding="utf8")
l = f.readlines()
word = 0
for i in range(len(l)):
    l[i] = l[i].rstrip()
    print(l[i])
    words = l[i].split()
    word += len(words)
print("�� ������ ��: %d"%len(l))
print("�� �ܾ��� ��: %d"%word)
f.close()
"""


f = open("smart_contact.txt","r",encoding="utf8")
dic={}

l = f.readlines()
for i in l:
    i = i.rstrip()
    words = i.split()
    for j in words:
        if j in dic:
            dic[j]+=1
        else:
            dic[j] =1
l = sorted(dic.values())
m = l[-1]
for k in range(m):
    for k,v in dic.items():
        if v==m:
            print("{} : {}".format(v,k),end=" ")
    m -= 1
    
print()
f.close()


"""
f = open("students.txt","r",encoding="utf8")
l = f.readlines()
dic = {}
for i in l:
    i = i.rstrip()
    i = i.split()
    dic[i[0]] = int(i[1])+int(i[2])+int(i[3])
print("="*13,"�л� �̸� (key ��) ���","="*13)
print(dic.keys())
print("="*13,"���� ���� (value ��) ���","="*13)
print(dic.values())
print("="*13,"�̸������� �����Ͽ� ���","="*13)
print("----- Name : Score -----")
l = sorted(dic.keys())
for i in range(len(dic)):
    print("{:>8} : {:<4}".format(l[i],dic[l[i]]))
"""

"""
import csv
f = open("dollar.csv")
csv_data = csv.reader(f)

for row in csv_data:
    for i in range(len(row)-1):
        print("{:>10}".format(row[i+1]),end=" ")
    print()
print("{:>7}".format("��ȭ��"),end=" ")
for i in range(len(row)-2):
    print("{:>10.2f}".format(float(row[i+2])-float(row[i+1])),end=" ")
"""

"""
while(True):
    try:
        n = int(input("���ڸ� �Է��ϼ���: "))
    except ValueError:
        print("������ �ƴմϴ�. �ٽ� �Է��Ͻÿ�.")
    else:
        print("���� �Է��� �����Ͽ����ϴ�!")
        break
"""

