#-*-coding:CP949-*-

"""
n1 =123
n2 = -123
n3 = 0
n4 =3.14
n5 = -3.14
n6 = 0.0
print(type(n1),type(n2),
type(n3),
type(n4),
type(n5),
type(n6))
"""

"""
complex j로 허수 i를 대신해서 표현함
n1= 10+30j
print(type(n1))
"""

"""
print("'test'")
print('"test"')
print("나는 현재"+str(21)+"살이다.")
"""

"""
s = 'abcdefghijklmn'
for i in range(len(s)):
    print(s[i])
for i in range(len(s)):
    print(i)

print(s[0:2])
#0부터 5미만 까지 2개씩 띄어서 출력
print(s[0:6:2])
"""
"""
name = input("안녕하세요 이름이 어떻게 되시나요? ")
print("반갑습니다 %s 씨" % name)
print("이름의 길이는 다음과 같군요: ",len(name))
age = int(input("나이가 어떻게 되나요?: "))
print("내년이면 ",age+1,"이 되시는군요")
"""

"""
print("가나다라",end='')
print("마바사")
"""
"""
year = int(input("오늘의 연도를 입력하시오: "))
month = int(input("오늘의 월를 입력하시오: "))
day= int(input("오늘의 일를 입력하시오: "))

print("오늘은 ",year,"년",month,"월",day,"일입니다.")
"""

"""
import time
now = time.time()
year = int(1970 +now//(365*24*3600))
print("올해는",year,"입니다.")
age = int(input("몇 살이신가요? "))
print("2050년에는",age+2050-year,"살 이시군요.")
"""

"""
print("소금물의 농도를 구하는 프로그램입니다")
gram = int(input("소금의 양은 몇 g입니까?" ))
water = int(input("물의 양은 몇 g입니까?" ))
print("소금물의 농도: %0.2f %%" % (gram/(water+gram)*100))
"""

"""
list = []
for i in range(5):
    list.append(input("친구의 이름을 입력하시오: "))
print(list)
"""

"""
list = []
list.append(input("이름은? "))
list.append(int(input("전화번호는? ")))
list.append(int(input("나이는? ")))

print(list)
"""

"""
c_num1 = 2.7 + 3.2j
c_num2 = 5.1 + -2.6j
print("덧셈 결과: %0.2f + %0.2fi "%( c_num1.real+c_num2.real,c_num1.imag+c_num2.imag))
print("뺄셈 결과: %0.2f + %0.2fi "%( c_num1.real-c_num2.real,c_num1.imag-c_num2.imag))
print("곱셈 결과: %0.2f + %0.2fi "%( c_num1.real*c_num2.real,c_num1.imag*c_num2.imag))
print("%0.1f + %0.1fi 복소수의 실수부분 : %0.2f"%(c_num1.real,c_num1.imag,c_num1.real))
print("%0.1f + %0.1fi 복소수의 실수부분 : %0.2f"%(c_num1.real,c_num1.imag,c_num1.imag))

print("%0.1f + %0.1fi 복소수의 켤레복소수 : %0.2f + %0.2fj"%(c_num2.real,c_num2.imag,c_num2.conjugate().real,c_num2.conjugate().imag))
print("%0.1f + %0.1fi 복소수의 크기 : %0.5f"%(c_num2.real,c_num2.imag,abs(c_num2)))

"""

"""
import datetime as dt

dt_now = dt.datetime.now()
print(dt_now)
print("오늘은 {0}년 {1}월 {2}일 입니다.".format(dt_now.year,dt_now.month,dt_now.day))
print("현재 시간은 {0}시 {1}분 입니다.".format(dt_now.hour,dt_now.minute))
print("한국식 표현(년/월/일): {0:04d}/{1:02d}/{2:02d}".format(dt_now.year,dt_now.month,dt_now.day))
print("미국식 표현(월/일/년): {1:02d}/{2:02d}/{0:04d}".format(dt_now.year,dt_now.month,dt_now.day))
print("영국식 표현(일/월/년): {2:02d}/{1:02d}/{0:04d}".format(dt_now.year,dt_now.month,dt_now.day))
"""

"""
import datetime as dt

td = dt.datetime.today()
print("오늘은 {0}년 {1:02d}년 {2:02}일 입니다.".format(td.year,td.month,td.day))
d_d = td+dt.timedelta(days=100)
print("100일 후는 {0}년 {1:02d}월{2:02d}일 입니다.".format(d_d.year,d_d.month,d_d.day))

"""

"""
import datetime as dt

year = int(input("출생년도를 입력하세요: "))
month = int(input("출생월을 입력하세요: "))
day = int(input("출생일을 입력하세요: "))
print("출생일({0}년{1}월{2}일)로 부터 {3},{4}일 지났습니다.".format(year, month, day, (dt.datetime.today() - dt.datetime(year,month,day)).days//1000,(dt.datetime.today() - dt.datetime(year,month,day)).days%1000 ))
"""

"""
import datetime as dt

n = int(input("오늘로 부터 몇일후를 알고 싶으신가요? "))
p_d = dt.datetime.today() + dt.timedelta(days=n)
print("오늘은 {0}년{1}월{2}일 입니다.".format(dt.datetime.today().year,dt.datetime.today().month,dt.datetime.today().day))
print("{3}일후는 {0}년{1}월{2}일 입니다.".format(p_d.year,p_d.month,p_d.day,n))
"""

"""
import datetime as dt
p = []
p.append(input("당신의 이름은? "))
p.append(int(input("당신의 나이는? ")))
p.append(float(input("당신의 키는? ")))
print(p)
print("안녕하세요 ",p[0])
print("2050년에는 {}살이 되시겠네요".format(p[1]+2050-dt.datetime.today().year))
print("남자 평균키인 175.5cm에 {0:0.1f}cm, 여성 평균키인 163.2cm에 {1:0.1f}cm차이가 나네요.".format(p[2]-175.5,p[2]-163.2))
"""

li = []
su = 0
avg = 0.0
for i in range(5):
    li.append(int(input("정수를 입력하시오:")))
    su += li[i]
avg = su/5
print(li)
print("데이터 합계: ",su)
print("데이터 평균: %0.2f"% avg)