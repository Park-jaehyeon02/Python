#-*-coding:CP949-*-

"""
Heroes = []
Heroes.append("아이언맨")
Heroes.append("닥터 스트레인지")
print(Heroes)

letters = ["A","B","C","D","E","F"]
print(letters[-3:-1])
print(letters[0:])
print(letters[:])
print(letters[:-2])



Heroes = ["아이언맨","토르","헐크","스칼렛 위치"]
Heroes[2] = "스파이더맨"
Heroes.append("슈퍼맨")
Heroes.insert(0,"배트맨")
Heroes.insert(3,"원더우맨")

Heroes.remove("스칼렛 위치")

#if "토르" in Heroes:
#    Heroes.remove("토르")


del Heroes[0]
print("del Heroes[0] :", Heroes)
Heroes.pop
print("Heroes.pop :", Heroes)
print("Heroes.index('슈퍼맨') : ",Heroes.index("슈퍼맨"))

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
sockdam.append("고생 없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다.")
sockdam.append("꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다.")
sockdam.append("사람은 사랑할 때 누구나 시인이 된다")
print("#"*20)
print("# 오늘의 속담 #")
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
    name = input("영웅들의 이름을 입력하시오: ")
    he.append(name)

for i in he:
    print(i,end=" ")


phone_book = {"홍길동" : "010-1234-5678"}
phone_book["강감찬"] = "010-1234-5679"
phone_book["이순신"] = "010-1234-5680"
print(phone_book)

print(phone_book["이순신"])
print(phone_book.keys())
print(phone_book.values())

phone_book = {"홍길동" : ["010-1234-5678",21]}
phone_book["강감찬"] = ["010-1234-5679",24]
phone_book["이순신"] = ["010-1234-5680",30]

print(phone_book["강감찬"][1])


phone_book = {"홍길동" : "010-1234-5678",
             "강감찬" : "010-1234-5679",
             "이순신" : "010-1234-5680"}

for key in sorted(phone_book.keys()):
    print(key,phone_book[key])

del phone_book["홍길동"]
print(phone_book)

print(phone_book.pop('이순신'))
print(phone_book)

phone_book = {"홍길동" : "010-1234-5678",
             "강감찬" : "010-1234-5679",
             "이순신" : "010-1234-5680"}
phone_book.clear()
print(phone_book)

phone_book = {"홍길동" : "010-1234-5678",
             "강감찬" : "010-1234-5679",
             "이순신" : "010-1234-5680"}
for i in phone_book.keys():
    print(i)
for i in phone_book.values():
    print(i)

for k,v in phone_book.items():
    print("{}의 전화번호는 {}입니다.".format(k,v))

sales = {"콜라" : "4","사이다" : "5","삼각김밥" : "10"}
print(sales[input("물건의 이름을 입력하시오: ")])

a = {"one":"하나","two":"둘","three":"셋"}
print(a[input("단어를 입력하시오: ")])
"""


"""
#실습 문제

ins = {"삽입" : 2,"삭제":1,"끝":0}
li = []
while(True):
    avg = 0
    g_ins = input("명령을 입력하세요: ")
    if 0==ins[g_ins]:
        break
    elif 1==ins[g_ins]:
        li.pop()
    elif 2==ins[g_ins]:
        li.append(int(input("데이터를 입력하세요: ")))
    for i in li:
        avg += i
    avg /= len(li)
    print(li,"avg:%0.2f" % avg)

s=[]
for i in range(5):
    s.append(int(input("성적을 입력하세요:")))
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
print("평균:%0.2f" % (n_sum/len(s)))
print("최고 점수:%d" % n_max)
print("최저 점수:%d" % n_min)
print("90점 이상 학생:%d명" % cnt)


data = []
for i in range(3):
    line=[]
    for j in range(2):
        line.append((i*10)+j)
    data.append(line)

print(data)


li = []
for i in range(5):
    hak = input("학번: ")
    name = input("이름: ")
    korean = int(input("국어: "))
    english =  int(input("영어: "))
    math = int(input("수학: "))
    li.append([hak,name,korean,english,math,korean+english+math])

print(li)
print("="*5+"이름순 정렬"+"="*5)

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
print("="*5+"성적순 정렬"+"="*5)
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
sorted(list , key=lambda x: x[1]) 1번 인ㄷ넥스르르 기준으로 오림차순으로 정렬

sorted(list , key=lambda x: -x[5]) 내림차순으로 정렬
"""

"""
li=[]
for i in range(3):
    tli=[]
    for j in range(3):
        tli.append(int(input("데이터를 입력하세요: ")))
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

d = {'a':"삽입","d":"삭제","s":"검색","p":"출력","e":"종료"}
li = []
while(True):
    ins = input("명령을 입력하세요: ")
    if d[ins] =="삽입":
       li.append(input("이름을 입력하세요: "),input("전화번호를 입력하세요: "))
    if d[ins] =="삭제":
        tmp = input("이름은 입력하세요: ")
        if tmp in li:
            for i in range(len(li)):
                if li[i][0]==tmp:
                    del li[i]
        else:
            print(tmp,"존재하지 않음!!")
    if d[ins] =="검색":
        tmp = input("이름은 입력하세요: ")
        if tmp in li:
           for i in range(len(li)):
                if li[i][0]==tmp:
                    print(li[i])

        else:
            print(tmp,"존재하지 않음!!")
    
    if d[ins] =="출력":
        
    if d[ins] =="종료":
         print("프로그램종료!!")
         break

"""
get 함수
"""