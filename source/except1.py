#-*-coding:CP949-*-

"""
#예외 처리
try:
    1/0
except ZeroDivisionError:
    print("0으로 나누는 예외")

try:
    1/0
except Exception as e:
    print(e)
"""

#다중 예외 처리
"""
try:
    5/3
except ZeroDivisionError:
    print("0으로 나눔")
except IOError:
    print("입출력 에러")
else:
    print("에러 없음")
finally:
    print("에러 상관 없이 실행됨")
"""

"""
f = open("data.txt","r",encoding="utf8")
cnt = 0
to = 0
for i in f:
    i = i.split()
    cnt += len(i)
    for j in i:
        to += int(j)
        if int(j)%2==0:
            print("%s: 짝수"%j)
        else:
            print("%s: 홀수"%j)
print("정수의 갯수: %d"% cnt)
print("정수의 갯수: %d"% to)
print("정수의 갯수: %.2f"% to/cnt)
f.close()
"""

"""
f = open("text.txt","r",encoding="utf8")
l = f.readlines()
word = 0
for i in range(len(l)):
    l[i] = l[i].rstrip()
    print(l[i])
    words = l[i].split()
    word += len(words)
print("총 문장의 수: %d"%len(l))
print("총 단어의 수: %d"%word)
f.close()
"""


f = open("smart_contact.txt","r",encoding="utf8")
dic={}

l = f.readlines()
for i in l:
    i = i.rstrip()
    words = i.split()
    for j in words:
        if j in dic:
            dic[j]+=1
        else:
            dic[j] =1
l = sorted(dic.values())
m = l[-1]
for k in range(m):
    for k,v in dic.items():
        if v==m:
            print("{} : {}".format(v,k),end=" ")
    m -= 1
    
print()
f.close()


"""
f = open("students.txt","r",encoding="utf8")
l = f.readlines()
dic = {}
for i in l:
    i = i.rstrip()
    i = i.split()
    dic[i[0]] = int(i[1])+int(i[2])+int(i[3])
print("="*13,"학생 이름 (key 값) 출력","="*13)
print(dic.keys())
print("="*13,"과목 총점 (value 값) 출력","="*13)
print(dic.values())
print("="*13,"이름순으로 정렬하여 출력","="*13)
print("----- Name : Score -----")
l = sorted(dic.keys())
for i in range(len(dic)):
    print("{:>8} : {:<4}".format(l[i],dic[l[i]]))
"""

"""
import csv
f = open("dollar.csv")
csv_data = csv.reader(f)

for row in csv_data:
    for i in range(len(row)-1):
        print("{:>10}".format(row[i+1]),end=" ")
    print()
print("{:>7}".format("변화율"),end=" ")
for i in range(len(row)-2):
    print("{:>10.2f}".format(float(row[i+2])-float(row[i+1])),end=" ")
"""

"""
while(True):
    try:
        n = int(input("숫자를 입력하세요: "))
    except ValueError:
        print("정수가 아닙니다. 다시 입력하시오.")
    else:
        print("정수 입력이 성공하였습니다!")
        break
"""

