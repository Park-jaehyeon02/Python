#-*-coding:CP949-*-

"""
def inch():
    v_inch = float(input("��ġ�� �Է��ϼ���: "))
    centi = 2.54*v_inch
    return v_inch, centi

def mile():
    v_mile = float(input("������ �Է��ϼ���: "))
    kilo = 1.61 * v_mile
    return v_mile, kilo

inch_1, centi1 = inch()
mile1, kilo1 = mile()
print("{:0.3f} ��ġ = {:0.3f} ��Ƽ����".format(inch_1,centi1))
print("{:0.3f} ���� = {:0.3f} ų�ι���".format(mile1,kilo1))

def collapse():
    cx1 = int(input("ù��° �� ������ x��ǥ: "))
    cy1 = int(input("ù��° �� ������ y��ǥ: "))
    cr1 = int(input("ù��° ���� ������: "))
    
    cx2 = int(input("�ι�° �� ������ x��ǥ: "))
    cy2 = int(input("�ι�° �� ������ y��ǥ: "))
    cr2 = int(input("�ι�° ���� ������: "))
    
    crd = cr1+cr2
    cr = ((cx1-cx2)**2 + (cy1-cy2)**2)**0.5
    print(cr,crd)
    if (crd < cr):
        print("��({},{})�� ��({},{}) ������ �Ÿ�: {:0.3f}".format(cx1,cy1,cx2,cy2,cr))
        print("�� �� ���� ������ �ֽ��ϴ�")
    else:
        print("��({},{})�� ��({},{}) ������ �Ÿ�: {:0.3f}".format(cx1,cy1,cx2,cy2,cr))
        print("�� �� ���� �浹�Ͽ����ϴ�")

collapse()


def one_step(n,c):
    print("{}:{}{}".format(n//10**c,n_list[n//10**c],p_list[c]))
    if c!=0:
        return one_step(n%10**c,c-1)
    else:
        return 0

p_list=["","��","��","õ","��","��","��","õ","��"]
n_list=["","��","��","��","��","��","��","ĥ","��","��"]
number = int(input("�ݾ��� ���ڷ� �Է�: "))
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
    pay_m = int(input("����� ���� [����:����]: "))
    pay_y = pay_m*12
    print("����(����): {:d},{:03d}����".format(pay_y//1000,int(pay_y%1000)))
    pay_y = int(tax(pay_m*12))
    print("�Ǽ��� ����(����): {:d},{:03d}����".format(pay_y//1000,int(pay_y%1000)))
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

n = int(input("1���� ��� ���������� �Ҽ��� ã���ð� �����Ű���?: "))
find_prime(n)


def func1():
    n = input("������ �Է��Ͻÿ�: ")

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

    print("��� : {:0.2f}".format(sum))
    print("�ִ�:",max)
    print("�ּ�:",min)

while(True):
    func1()

def read_data(pyth_list,data_list,comp_list):
    pyth_list.append(int(input("���̽� ����: ")))
    data_list.append(int(input("�ڷᱸ�� ����: ")))    
    comp_list.append(int(input("��ǻ�Ͱ��� ����: ")))
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