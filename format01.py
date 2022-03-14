# -*- coding: CP949 -*-
#Ci Pal 949

a = 1
b = 2
print("0 : {0} 더하기 {1}은 {2}입니다.".format(a,b,a+b))
#{}생략가능 순차적으로 매칭
print("1 : {} 더하기 {}은 {}입니다.".format(a,b,a+b))
#인덱스 값 대신 이름을 지정하여 값을 매칭 시킬수 도 있음 가독성
print("3 : 연도 :{year} 지역 :{area}".format(year=2022,area="아산"))

#이름으로 지정할 경우 반드시 키이름을 매칭시켜줘야함 그렇지 않으면 KeyyError 발생
try:
    print("3 : 연도 :{year} 지역 :{area}".format(2022,"아산"))
except KeyError as err:
    print("Exception : ",err)

#중괄호를 출력하려면 중괄호를 2번 사용
print("{{중괄호 출력한다~}}, 올해는 몇년? : 바로 {{{}}}년~".format(2022))

#좌우정렬, 중렬정렬 -> ???????
print("좌측 정렬 |{0:<20}|".format("물체"))
print("우측 정렬 |{0:>20}|".format("물체"))
print("중앙 정렬 |{0:^20}|".format("물체"))