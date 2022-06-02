#-*-coding:CP949-*-

"""
class Car():
    color2 = "red"
    model2 = "C-Class"
    def drive(self):
        self.speed = 10

myCar = Car()
myCar.color="blue"
myCar.model= "E-Class"

myCar.drive()
print(myCar.speed)
print(myCar.color2)
print(myCar.color)
print(myCar.model)
print(myCar.model2)
"""

"""
class Car:
    def drive(self):
        self.speed = 10

myCar = Car()
myCar.speed=0
myCar.model = "E-Class"
myCar.color = "blue"
myCar.year="2017"

print("�ڵ��� ��ü�� �����Ͽ����ϴ�.")
print("�ڵ����� �ӵ���",myCar.speed)
print("�ڵ����� ������",myCar.color)
print("�ڵ����� ����",myCar.model)
print("�ڵ����� �����մϴ�.")
myCar.drive()
print("�ڵ����� �ӵ���",myCar.speed)
"""

"""
class Car:
    def __init__(self,speed,color,model):
        self.speed= speed
        self.color = color
        self.model = model

    def drive(self):
        self.speed=60

myCar = Car(0,"blue",'E-Class')
print("�ڵ��� ��ü�� �����Ͽ����ϴ�.")
print("�ڵ����� �ӵ���",myCar.speed)
print("�ڵ����� ������",myCar.color)
print("�ڵ����� ����",myCar.model)
print("�ڵ����� �����մϴ�")
myCar.drive()
print("�ڵ����� �ӵ���",myCar.speed)


yourCar = Car(20,"red",'C-Class')
print("�ڵ��� ��ü�� �����Ͽ����ϴ�.")
print("�ڵ����� �ӵ���",yourCar.speed)
print("�ڵ����� ������",yourCar.color)
print("�ڵ����� ����",yourCar.model)
print("�ڵ����� �����մϴ�")
yourCar.drive()
print("�ڵ����� �ӵ���",yourCar.speed)
"""

"""
class Counter:
    def __init__(self):
        self.count = 0
    def reset(self):
        self.count = 0
    def increment(self):
        self.count +=1
    def get(self):
        return self.count

myCount = Counter()
print(myCount.get())
for i in range(50):
    myCount.increment()
print(myCount.get())
myCount.reset()
print(myCount.get())
"""
"""
class Television:
    def __init__(self,channel,volume,on):
        self.channel = channel
        self.volume = volume
        self.on = on
    def show(self):
        print(self.channel,self.volume,self.on)
    def setChannel(self,channel):
        self.channel = channel
    def getChannel(self):
        return self.channel

myTv = Television(11,100,True)
myTv.show()
myTv.setChannel(9)
myTv.show()
"""

"""
class t:
    def __init__(self):
        self.__t = 0
        self.t2=1
a = t()
print(a.t2)
print(a.__t)
"""

"""
#__Val �� �����ϱ� ���ؼ��� Ŭ���������� �����ؼ� �������ִ� 
#�Լ��� �ʿ�
class Student:
    def __init__(self,name=None,age=0):
        self.__name = name
        self.__age = age

    def getAge(self):
        return self.__age
    def getName(self):
        return self.__name
    def setAge(self,age):
        self.__age = age
    def setName(self,name):
        self.__name = name

obg=Student("Hong",20)
print(obg.getName())
"""
"""
#__str__() �޼ҵ� 
class Car():
    def __init__(self,speed,color,model):
        self.speed = speed
        self.color = color
        self.model = model

    def __str__(self):
        msg = "�ӵ�"+str(self.speed)+"���� "+self.color+" ��"+self.model
        return msg

dadCar = Car(0,"silver","A6")
momCar = Car(0,"white","520d")
myCar = Car(0,"blue","E-Class")
print(momCar)
"""

"""
class Rectangle:
    def __init__(self,side=0):
        self.side = side

    def getArea(self):
        return self.side**2

def printAreas(r,n):
    while n>=1:
        print(r.side,"\t",r.getArea())
        r.side = r.side +1
        n -=1
myRect = Rectangle()
count = 5
printAreas(myRect,count)
print("�簢���� ��", myRect.side)
print("�ݺ�Ƚ��=",count)
"""

from turtle import *
class Ball:
    def __init__(self,color,size,speed):
        self.x = 0
        self.y=0

        self.xs = speed
        self.ys = speed

        self.size = size
        self.color = color

        self.turtle = Turtle()
        self.turtle.shape('circle')
        self.turtle.color(color,color)
        self.turtle.resizemode("user")
        self.turtle.shapesize(size,size,10)

    def move(self):
        self.x +=self.xs
        self.y +=self.ys
        self.turtle.goto(self.x,self.y)

ball = Ball("red",2,1)
for i in range(100):
    ball.move()