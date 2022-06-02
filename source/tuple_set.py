#-*-coding:CP949-*-

"""
t = ()
t2 = (1,) #1개 만들때는 컴마를 해줘야 함안하면 정수가 할당됨
i = (1)
t3 = (1,2,3,4)
t4 = 1,2,3,4
li = [1,2,3,4]
t5 = tuple(li)
t6 = t3+t4 #더하기 연산은 합쳐짐
print(t,t2,t3,t4,t5,i)
print(type(i))
"""
"""
student = ("철수",19,"CS")
(name,age,major) = student
print(name,"\n",age,"\n",major)
t = (10,20,30,40,50,60,10,20,60,10)
print(t.count(10))
print(t.index(60))
"""
"""
r = float(input("원의 반지름을 입력하시오: "))
cir = (3.)
"""

"""
print("관리자 계정 생성 프로그램입니다.")
account = []
account.append(input("관리자 아이디 입력: "))
account.append(input("관리자 비밀번호 입력: "))
while(True):
    account.append(input("관리자 아이디 입력: "))
    if account[1]==account[2]:
        print("계정이 성공적으로 생성되었습니다.")
        break
    else:
        del account[2]
        print("비밀번호가 서로 다릅니다.")
t_a = tuple(account)
print(t_a)
"""

"""
#세트(set)
numbers = {2,1,3}
print(numbers)
print(len(numbers))
fruits = {"apple","banana"}
# 세트는 인덱스 접근이 불가능함
numbers.add(4)
print(numbers)
numbers.discard(2)
print(numbers)
numbers.remove(1)
print(numbers)
numbers.clear()
print(numbers)
"""

"""
add
discard
clear
union 합집합
difference 차집합
intersection 교집합
symetric_difference 대칭 차집합
issubset 부분집합
"""

"""
s1 = {1,3,5,7}
s2 = {2,4,7,9}
union = s1.union(s2) # s1 | s2
print("s1 | s2 =",union)
intersec = s1.intersection(s2) # s1& s2
print("s1 & s2 =",intersec)
diff = s1 -s2 
print("s1 - s2=",diff)
dym_diff = s1 ^ s2 #s1.dsymmetric_difference(s2)
print("s1 ^ s2 =",dym_diff)
"""

"""
s1 = {1,3,5,7,8}
s2 = {2,4,7,8,9}
s3 = {5,6,8,10}
union = s1 | s2 | s3
print(union)
intersec = s1 & s2 & s3
print(intersec)
diff = s1 -s2 - s3
print(diff)
dym_diff = s1 ^ s2 ^ s3
print(dym_diff) # 왜 8이 출력되는지 생각해 보자
"""

"""
s1= {1,3,5,7,8}
s2 = {2,4,7,8,}
s3 = {5,8}
s4 = {6,9}
sub_set = s2.issubset(s1) # s2가 s1으 ㅣ부분집합
print(sub_set)
sub_set = s3.issubset(s1) # s3가 s1으 ㅣ부분집합
print(sub_set)
sup_set = s1.issuperset(s2) # 상위집합
print(sup_set)
sup_set = s1.issuperset(s3) # 상위집합
print(sup_set)
dis_join = s1.isdisjoint(s2) # 서로소
print(dis_join)
dis_join = s1.isdisjoint(s2) # 서로소
print(dis_join)
"""

"""
a = {"홍길동","이순신","김유신","강감찬"}
b = {"이순신","김유신","하하하"}
print(a&b)
"""

"""
s1 = "hello everyone"
s2= "Have a great day!!"
li = list(set(s1)&set(s2))
print(li)
"""
s1 = "샌디에이고 파드리스 김하성이 시즌 첫 홈런을 터뜨렸다. 김하성은 21일(한국시간) 미국 캘리포니아주 샌디에이고 펫코 파크에서 열린 신시내티 레즈와의 경기에서 9번 3루수로 선발출전했다."
se = set(s1.split(" "))
print("사용된 단어수:",len(s1.split(" ")))
print(se)
