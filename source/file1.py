#-*-coding:CP949-*-

"""
f = open("test.txt","r",encoding="utf8")
print(f.read(1))
print("@@")
print(f.read(1000))
f.close()

f = open("test.txt","r",encoding="utf8")
print(f.readlines())

f = open("test.txt","r",encoding="utf8")
print(f.readline(5))
f.close()

f = open("test.txt","r",encoding="utf8")
for l in f:
    #rstrip ���Ͽ��� ���پ� �о�ͼ� �ٹٲ� ��ȣ�� ������
    l = l.rstrip()
    print(l)
f.close()

f = open("phone1.txt","w",encoding="utf8")
f.write("ȫ�浿\n")
f.write("ȫ�ڰ�\n")
f.write("��ö��")
f.write("asdf\n")
f.close()

f = open("phone1.txt","w",encoding="utf8")
f.write("������")
f.write("������")
f.write("\n\n\n\n\n")
f.close()

a = "word is word! test"
print(a.split())
"""

f = open("proverbs.txt","r",encoding="utf8")
for l in f:
    l = l.rstrip()
    words = l.split()
    for i in words:
        print(i)

f.close()