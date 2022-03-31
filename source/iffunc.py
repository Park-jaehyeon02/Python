#-*-coding:CP949-*-

"""
n = int(input("연도를 입력하세요:"))

if n%4==0 and n%100 != 0 or n%400==0:
    print("{0}년은 윤년입니다.".format(n))
else:
    print("{0}년은 윤년이 아닙니다.".format(n))

"""

"""
import random

n = random.randrange(2)
print("동전 던지기 게임을 시작합니다.")

if n==0:
    print("뒷면입니다.")
else:
    print("앞면입니다.")

print("게임이 종료되었습니다.")
"""

"""
import random
time =  random.randint(1,24)
sunny = random.choice([True,False])

print("좋은 아침입니다. 지금 시각은 ",time,"시입니다.")
"""

"""
import random
a = int(input("변a의 길이: "))
b = int(input("변b의 길이: "))
c = int(input("변c의 길이: "))

if (c**2==a**2+b**2):
    print("직각삼각형입니다.")
else:
    print("직각삼각형이 아닙니다.")

"""

"""
h = float(input("당신의 키는? : "))
g = input("당신의 성별은? 남성 or 여성 : ")

if (g=="남성"):
    if (h>=173.5):
        print("당신은 평균키 이상입니다.")
    else:
        print("당신은 평균키 미만입니다.")
else:
    if (h>=163.2):
        print("당신은 평균키 이상입니다.")
    else:
        print("당신은 평균키 미만입니다.")

"""

"""
n = int(input("정수를 입력하세요 : "))

print("20은",end='')
if (n%4==0):
    print("4의 배수입니다.")
elif (n%5==0):
    print("5의 배수입니다.")
elif (n%4==0 and n%5==0):
    print("4의 배수이면서 5의 배수입니다.")
else:
    print("4, 5 둘다의 배수도 아닙니다.")
"""

"""
a = int(input("나이를 입력하세요 : "))
h = float(input("키를 입력하세요 : "))

if (a>=10 and h>=165):
    print("놀이기구를 이용할수 있습니다.")
else:
    if(a<10 and h<165):
        print("{}살이고 {}cm 키는 놀이기구를 이용하실수 없습니다.".format(a,h))
    elif (a<10):
        print("{}살은 놀이기구를 이용하실수 없습니다.".format(a))
    else:
        print("{}cm 키는 놀이기구를 이용하실수 없습니다.".format(h))
"""

"""
import datetime as dt
d = dt.datetime.now()

d_dic={0:"월요일",1:"화요일",2:"수요일",3:"목요일",4:"금요일",5:"토요일",6:"일요일"}
print("지금은 {}년 {}월 {}일 {}".format(d.year, d.month, d.day, d_dic[d.weekday()]),end='')
if (d.time().hour>=12):
    print("오후 ",end='')
    if(d.time().hour==12):
        print("{}시 {}분 입니다.".format(d.time().hour, d.time().min))
    else:
        print("{}시 {}분 입니다.".format(d.time().hour-12, d.time().minute))
"""

s1 = int(input("파이썬 점수를 입력하세요: "))
s2 = int(input("C언어 점수를 입력하세요: "))
s3 = int(input("컴퓨터개론 점수를 입력하세요: "))

t = s1+s2+s3
a = t/3

print("총점: ",t)
print("평균: %0.2f"%a)

if (a>=90):
    print("A학점 입니다")
    print("성적우수 장학생입니다.")
elif (a>=80):
    print("B학점 입니다")
    print("우수한 성적입니다.")
elif (a>=70):
    print("C학점 입니다")
    print("조금더 노력해야 합니다.")
elif (a>=60):
    print("D학점 입니다")
    print("열심히 노력해야 합니다.")
else:
    print("F학점 입니다")
    print("다음에 재수강 해야합니다")
