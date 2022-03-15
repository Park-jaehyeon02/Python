# -*- coding: CP949 -*-
#좌우정렬, 중렬정렬 -> ???????
print(10**19)
print("좌측 정렬 |{0:<20}|".format("물체"))
print("우측 정렬 |{0:>20}|".format("물체"))
print("중앙 정렬 |{0:^20}|".format("물체"))

print("여러 문자 |{0:+^20}|".format("물체"))
print("여러 문자 |{0:=^20}|".format("물체"))
print("여러 문자 |{0:$^20}|".format("물체"))

#F-string format
year = 2019
area = "아산"
print(f"나는 {area}에 살고있어요")

str = f"나는 {area}에 살고있어요"
print(str)

list = [10,20,30,40,50]
dict = {"name":"IU","area":"서울"}
print(f'리스트 : {list[0]},{list[1]},{list[2]}')
#""을 사용할 때 print의 문자열과 안겹치게 주의 SyntaxError!
#ex) " dict['key'] " or ' dict["key"]'
print(f'이름 : {dict["name"]}, 사는곳 :{dict["area"]}')