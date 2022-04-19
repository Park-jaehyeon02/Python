#-*-coding:CP949-*-

"""
r = float(input("반지름을 입력하세요: "))
v = 4/3 * 3.141592 * r**3
print("구의 부피 = %0.3f" %(v))
"""

"""

x = int(input("x의 값을 입력하세요: "))
y = 2*x**3 + 3*x**2 + 7*x +10
print("2*",x,"^3 + 3*",x,"^2 + 7*",x,"+10 = ",y)

format 형식으로 작성하면 더 깔끔하게 나올것 같았음
x = int(input("x의 값을 입력하세요: "))
y = 2*x**3 + 3*x**2 + 7*x +10
print("2*{0}^3+3*{0}^2+7*{0}+10 = {1}".format(x,y))
더 깔끔한 듯?
"""

"""
y = int(input("예금 경과 년수를 입력하세요:"))
r = float(input("예금 금리(%)를 입력하세요:"))
o = int(input("예금 원금을 입력하세요:"))
re = o * ( (1 + r/100) ** y)
print("총 받을 금액: %d원" % re)
"""

"""
put = int(input("지폐로 교환할 돈을 입력하세요: "))
five = put//50000
put %= 50000
ttho = put//10000
put %= 10000
ftho = put//5000
put %= 5000
tho = put//1000
put %= 1000
print("5만원 지폐:%d장"% five)
print("1만원 지폐:%d장"% ttho)
print("5천원 지폐:%d장"% ftho)
print("1천원 지폐:%d장"% tho)
print("나머지 잔돈: %d원" % put)
"""

"""
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

val = 2*(x**3)+ 3*(x**2)*(y**2) + 7*x*(z**3) - 5*y
val2 = (x+y)/(2*x*z)
print("2*{0}^3+3*{0}^2*{1}^2+7*{0}*{2}^3-5*{1} = {3:0.2f}".format(x,y,z,val))
print("{0} + {1} / 2*{0}*{1} = {2:0.2f}".format(x,z,val2))
"""

"""
x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))
r = ((x2-x1)**2 + (y2-y1)**2))**0.5
print("두 점 사이의 거리:%.2f" % r)
"""



x = int(input("x: "))
y = int(input("y: "))

print("x:",bin(x))
print("y:",bin(y))
print("&: ",bin(x&y),"=>",x&y)
print("|: ",bin(x|y),"=>",x|y)
print("^: ",bin(x^y),"=>",x^y)
