#-*-coding:CP949-*-

"""
f = open("password.txt","r",encoding="utf8")
(r_id,r_pass) = tuple(f.readline().split(" "))
print("관리자 정보를 성공적으로 조회하였습니다.")
print(r_id,r_pass)
while True:
   m_id = input("아이디 입력: ")
   m_pass = input("비밀번호 입력: ")
   if (m_id==r_id and m_pass ==r_pass):
       print("로그인에 성공하였습니다.")
       break
   else:
       print("아이디 또는 비밀번호가 잘못 입력되었습니다.")
"""

"""
f = open("Goldensaying.txt","r",encoding="utf8")
li=[]
for i in f:
    i = i.rstrip('\n')
    li.append(i)
print("첫번째 명언: ",li[0])
print("두번째 명언: ",li[1])
m1_set = set(li[0].split(" "))
m2_set = set(li[1].split(" "))

print("첫번째 명언 집합: ",m1_set)
print("두번째 명언 집합: ",m2_set)
print("공통 단어: ",m1_set.intersection(m2_set))
f.close()
"""

"""
f1 = open("sample1.txt","r",encoding="euc-kr")
f2 = open("sample2.txt","r",encoding="euc-kr")
li1=[]
li2=[]
count = [0,0]
print("="*4+" 1번 파일 "+"="*4)
for i in f1:
    i = i.rstrip()
    count[0] +=1
    count[1] +=len(i.split())
    for j in i.split():
        li1.append(j)
print("총 문장의 수:",count[0])
print("총 단어의 수:",count[1])

count = [0,0]
print("="*4+" 2번 파일 "+"="*4)
for i in f2:
    i = i.rstrip()
    count[0] +=1
    count[1] +=len(i.split())
    for j in i.split():
        li2.append(j)
print("총 문장의 수:",count[0])
print("총 단어의 수:",count[1])
set1=set(li1)
set2=set(li2)
print("="*5+" 파일 비교 "+"="*5)
inter = set1&set2
print("같은 단어의 수:",len(inter))
print("공통 단어: ",inter)
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

print("총 문장의 수: ",count[0])
print("총 단어의 수: ",count[1])
print("중복제거 단어의 수: ",len(m_set))
print("중복 단어 비율: %0.2f%%"% ((count[1]-len(m_set))/count[1]*100))
f.close()
"""

