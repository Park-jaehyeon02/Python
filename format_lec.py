
# -*- coding: CP949 -*-

#format 공부


year = 2022
month = 3 
day = 15
day_week = "화"
temp = 15.3
a
print("{y}년{m}월{d}일{dw}요일입니다.".format(m=month,d=day,dw=day_week,y=year))
print("{0:02d}월{1}은{2}요일은 온도가 {3:.2f}도입니다.".format(month,day,day_week,temp))


print("한국식 표현 (년/월/일/요일) : {0}/{1}/{2}/{3}".format(year,month,day,day_week))
print("미국식 표현 (요일/월/일/년) : {3}/{1}/{2}/{0}".format(year,month,day,day_week))
print("영국식 표현 (요일/일/월/년) : {3}/{2}/{1}/{0}".format(year,month,day,day_week))
""" 

# 정렬 문제
"""
number = 12345
print("출력연습:\b",10**9)
print("좌측정렬:{0:*<10}".format(number))

print("중앙정렬:{0:0^10}".format(number))

print("우측정렬:{0:=>10}".format(number))


n = "*****"
print("{0:>7}".format(n))
print("{0:^7}".format(n))
print("{0:<7}".format(n))

temp_str = "*"*5
print(temp_str)