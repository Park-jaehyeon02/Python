# -*-coding:CP949-*-

"""
복합 연산자
compound operator



x= 1000
print("초기값 x=",x)
x += 2
print("x += 2 :",x)
x -= 2
print("x -= 2 :",x)


#우선 연산자 문제
x = int(input("첫 번째 수를 입력하시오 :"))
y = int(input("두 번째 수를 입력하시오 :"))
z = int(input("세 번째 수를 입력하시오 :"))
avg = (x + y + z) /3
print("평균 : ",avg)


#관계 연산자
a,b = 100,200
print(a==b,a !=b,a>b,a<b,a>=b,a<=b)

a = 99
print((a>100) and (a<200))
print((a>100) or (a<200))
print(not(a==100))


#bit 논리곱 & ->bit단위로 and
print(10 & 7)
print(123 & 456)
print(0xffff & 0x00000)

#bit 논리합 | -> bit단위로 or
print(10 | 7)
print(123 | 456)
print(0xffff | 0x0000)

#비트 배타적 논리합 ^ 연산자 
print(10 ^ 7)
print(123 ^ 456)
print(0xffff ^ 0x0000)

#bit 부정 연산자 ~
a =12345
~a + 1
print(a)
#? -12345 안나옴

#왼쪽 시프트 연산자 <<
#2bit 시프트 하면 앞비트 2개는 사라지고 뒤에 00이 더해짐
#n시프트 하면 2^n을 곱하는 효과가 남
a = 10
print(a<<1,a<<2,a<<3,a<<4)

"""
#오른쪽 시프트 연산자 >>
#2^n으로 나누는 효과가 나타남
#몫만 남는 효과가 나타남

a = 10
print(a>>1,a>>2,a>>3,a>>4)
"""