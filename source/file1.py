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

f = open("proverbs.txt","r",encoding="utf8")
for l in f:
    l = l.rstrip()
    words = l.split()
    for i in words:
        print(i)

f.close()

fn = input("입력 파일 이름: ")
cn = input("출력 파일 이름: ")

f = open("input.txt","r",encoding="utf8")
fc = open("input_c.txt","w",encoding="utf8")
for l in f:
    fc.write(l)

f.close()
fc.close()
ml = []

f = open("input.txt","r",encoding="utf8")
for l in f:
    l = l.rstrip()
    ls = l.split()

    for i in range(len(ls)):
        ls[i] = ls[i].lower()
        ls[i] = ls[i].strip(',')
        ls[i] = ls[i].strip('.')


    #빈도 분석 교수님은 dict로 구현함
    for j in ls:
        ch = True
        for i in range(len(ml)):
            if ml[i][0] == j:
                ml[i][1] += 1
                ch = False
                break
        if ch:
            ml.append([j,1])

fw = open("output.txt","w",encoding="utf8")
for i in ml:    
    fw.write(str(i[0])+" "+str(i[1])+"\n")
fw.close()
f.close()
"""

