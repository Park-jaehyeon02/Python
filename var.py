# -*- coding: CP949 -*-
# -*- coding: "utf-8" -*-
"""
p = int(input("분자를 입력하세요 : "))
q = int(input("분모를 입력하세요 : "))
print(p,"/",q,"나눗셈의 몫 : ",p/q)
print(p,"/",q,"나눗셈의 몫 : ",p//q) 
print(p,"/",q,"나눗셈의 나머지 : ",p%q)

n = int(input("정수를 입력하세요 : "))
print(n%2)

n = int(input("초를 입력하세요 : "))
m = n//60
s = n%60
print(m,"분",s,"초")


a = int(input("아메리카노 판매 개수 :"))
c = int(input("카페라떼 판매 개수 :"))
ch = int(input("카푸치노 판매 개수 :"))
print("총 매출은 ",(a*2000+c*3000+ch*3500)//1000,",%03d" % ((a*2000+c*3000+ch*3500)%1000),"입니다.")

f-string!
공부


f = int(input("화씨온도: "))
c = (f-32)*5/9
print("섭씨온도: ",c)


weight = float(input("몸무게를 kg 단위로 입력하시오 : "))
height = float(input("키를 미터 단위로 입력하시오 : "))
bmi = weight/(height**2)
print("당신의 BMI=",bmi)

n = int(input("투입한 돈: "))
cost = int(input("물건값: "))
print("거스름돈: ",n-cost)
ch = n-cost

print("500원 동전의 개수:",ch//500)
print("100원 동전의 개수:",(ch%500)//100)
"""

a=1000
r=0.05
n=10

print(a*(1+r)**n)