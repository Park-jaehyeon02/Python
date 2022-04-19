#-*-coding:CP949-*-

"""
def inch():
    v_inch = float(input("인치를 입력하세요: "))
    centi = 2.54*v_inch
    return v_inch, centi

def mile():
    v_mile = float(input("마일을 입력하세요: "))
    kilo = 1.61 * v_mile
    return v_mile, kilo

inch_1, centi1 = inch()
mile1, kilo1 = mile()
print("{:0.3f} 인치 = {:0.3f} 센티미터".format(inch_1,centi1))
print("{:0.3f} 마일 = {:0.3f} 킬로미터".format(mile1,kilo1))

def collapse():
    cx1 = int(input("첫번째 원 중점의 x좌표: "))
    cy1 = int(input("첫번째 원 중점의 y좌표: "))
    cr1 = int(input("첫번째 원의 반지름: "))
    
    cx2 = int(input("두번째 원 중점의 x좌표: "))
    cy2 = int(input("두번째 원 중점의 y좌표: "))
    cr2 = int(input("두번째 원의 반지름: "))
    
    crd = cr1+cr2
    cr = ((cx1-cx2)**2 + (cy1-cy2)**2)**0.5
    print(cr,crd)
    if (crd < cr):
        print("점({},{})와 점({},{}) 사이의 거리: {:0.3f}".format(cx1,cy1,cx2,cy2,cr))
        print("두 원 서로 떨어져 있습니다")
    else:
        print("점({},{})와 점({},{}) 사이의 거리: {:0.3f}".format(cx1,cy1,cx2,cy2,cr))
        print("두 원 서로 충돌하였습니다")

collapse()


def one_step(n,c):
    print("{}:{}{}".format(n//10**c,n_list[n//10**c],p_list[c]))
    if c!=0:
        return one_step(n%10**c,c-1)
    else:
        return 0

p_list=["","십","백","천","만","십","백","천","억"]
n_list=["","일","이","삼","사","오","육","칠","팔","구"]
number = int(input("금액을 숫자로 입력: "))
one_step(number,len(str(number))-1)


def tax(pay_y):
    if (pay_y>100000):
        tax_i = pay_y* 0.45 - 6540
        return (pay_y - tax_i)
    elif (pay_y>50000):
        tax_i = pay_y*0.42-3540
        return (pay_y-tax_i)
    elif (pay_y>30000):
        tax_i = pay_y*0.40-2540
        return (pay_y-tax_i)
    elif (pay_y>15000):
        tax_i = pay_y*0.38-1940
        return (pay_y-tax_i)
    elif (pay_y>8800):
        tax_i = pay_y*0.35-1490
        return (pay_y-tax_i)
    elif (pay_y>4600):
        tax_i = pay_y*0.24-522
        return (pay_y-tax_i)
    elif (pay_y>1200):
        tax_i = pay_y*0.15-108
        return (pay_y-tax_i)
    else:
        return (pay_y - pay_y*0.06)

while(True):
    pay_m = int(input("월평균 월급 [단위:만원]: "))
    pay_y = pay_m*12
    print("연봉(세전): {:d},{:03d}만원".format(pay_y//1000,int(pay_y%1000)))
    pay_y = int(tax(pay_m*12))
    print("실수령 연봉(세후): {:d},{:03d}만원".format(pay_y//1000,int(pay_y%1000)))
    print()

def find_prime(num):
    prime = [2]
    for i in range(2,num+1):
        for j in prime:
            if i%j==0:
                break
            elif j == prime[-1]:
                prime.append(i)
    print(1,end=" ")
    for i in prime:
        print(i,end=" ")

n = int(input("1부터 어느 범위까지의 소수를 찾으시고 싶으신가요?: "))
find_prime(n)


def func1():
    n = input("정수를 입력하시오: ")

    sum = 0
    max = 0
    min = int(n.split(" ")[0])
    for i in (n.split(" ")):
        sum += int(i)
        if max<int(i):
            max = int(i)
        if min>int(i):
            min = int(i)
    sum /=len(n.split(" "))

    print("평균 : {:0.2f}".format(sum))
    print("최대:",max)
    print("최소:",min)

while(True):
    func1()

def read_data(pyth_list,data_list,comp_list):
    pyth_list.append(int(input("파이썬 점수: ")))
    data_list.append(int(input("자료구조 점수: ")))    
    comp_list.append(int(input("컴퓨터개론 점수: ")))
    return (pyth_list,data_list,comp_list)

def compute_data(pyth_list,data_list,comp_list,tot_list,score_list,st_num=5):
    avg = []
    avg.append(0)
    for j in pyth_list:
        avg[-1]+=j
    avg[-1]/=st_num
    avg.append(0)
    for j in data_list:
        avg[-1]+=j
    avg[-1]/=st_num
    avg.append(0)
    for j in comp_list:
        avg[-1]+=j
    avg[-1]/=st_num

    return avg

def decide_score(avg):
    if avg>90:
        print("A")

while(True):
    pyth_list=[]
    data_list=[]
    comp_list=[]
    for i in range(5):
        pyth_list,data_list,comp_list = read_data(pyth_list,data_list,comp_list)

"""

print(bin(123))