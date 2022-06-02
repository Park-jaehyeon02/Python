#-*-coding:CP949-*-
import math
"""
class Box:
    def __init__(self,w=0,h=0,l=0):
        self.w,self.h,self.l = w,h,l
    def __str__(self):
        return "("+str(self.w)+","+str(self.h)+","+str(self.l)+")"
    def volume(self):
        return self.w*self.h*self.l

b1 = Box(100,100,100)
print(b1)
print("상자의 부피는",b1.volume())
"""
"""
class Circle:
    def __init__(self,r=0):
        self.__radius = r
    def getr(self):
        return self.__radius
    def setr(self,r=0):
        self.__radius = r
    def area(self):
        return math.pi*(self.__radius**2)
    def length(self):
        return 2*math.pi*self.__radius

c = Circle(10)
print("원의 반지름=",c.getr())
print("원의 넓이=",c.area())
print("원의 둘레=",c.length())
"""

"""
class Bank:
    def __init__(self,balance=0):
        self.__balance = balance
    def withdraw(self,m=0):
        print("통장에서 %d 가 출금되었음"%m)
        self.__balance -=m
    def deposit(self,m = 0):
        print("통장에 %d 가 입금되었음"%m)
        self.__balance += m
    def __str__(self):
        return '현재 잔액은 %d 원입니다.'%self.__balance
b1 = Bank(10000)
print(b1)
b1.withdraw(1000)
print(b1)
b1.deposit(10)
print(b1)
"""

"""
class Dog:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def __str__(self):
        return str(self.__name)+' '+str(self.__age)

d1=Dog('Missy',3)
d2=Dog('Lucky',5)
print(d1)
print(d2)

class Car:
    def __init__(self,v,g,c):
        self.__velocity = v
        self.__gear = g
        self.__color = c
    def __str__(self):
        return "(%d,%d,%s)"%(self.__velocity,self.__gear,self.__color)
    def upgear(self):
        self.__gear+=1
    def downgear(self):
        self.__gear-=1
    def upspeed(self,s=1):
        self.__velocity+=s
    def downspeed(self,s=1):
        self.__velocity-=s

car1 = Car(100,3,'white')
print(car1)
car1.upgear()
print(car1)
car1.downgear()
print(car1)
car1.upspeed(10)
print(car1)
car1.downspeed(5)
print(car1)
"""

class Car:
    speed = 0
    def ups(self,v):
        self.speed +=v
    def downs(self,v):
        self.speed-=v

class Sedan(Car):
    seatNum=0
    def getSeatNum(self):
        return self.seatNum

class Truck(Car):
    capacity =0
    def getCapacity(self):
        return self.capacity

sedan1,truck1= Sedan(),Truck()
sedan1.ups(100)
truck1.ups(80)

sedan1.seatNum=5
truck1.capacity = 50
print(sedan1.speed,sedan1.getSeatNum())
print(truck1.speed,truck1.getCapacity())