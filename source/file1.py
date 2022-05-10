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
    #rstrip 파일에서 한줄씩 읽어와서 줄바꿈 기호를 삭제함
    l = l.rstrip()
    print(l)
f.close()

f = open("phone1.txt","w",encoding="utf8")
f.write("홍길동\n")
f.write("홍자공\n")
f.write("김철자")
f.write("asdf\n")
f.close()

f = open("phone1.txt","w",encoding="utf8")
f.write("강감찬")
f.write("김유신")
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