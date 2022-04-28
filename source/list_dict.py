#-*-coding:CP949-*-

"""
Heroes = []
Heroes.append("아이언맨")
Heroes.append("닥터 스트레인지")
print(Heroes)

letters = ["A","B","C","D","E","F"]
print(letters[-3:-1])
print(letters[0:])
print(letters[:])
print(letters[:-2])

"""

Heroes = ["아이언맨","토르","헐크","스칼렛 위치"]
Heroes[2] = "스파이더맨"
Heroes.append("슈퍼맨")
Heroes.insert(0,"배트맨")
Heroes.insert(3,"원더우맨")

Heroes.remove("스칼렛 위치")

#if "토르" in Heroes:
#    Heroes.remove("토르")


del Heroes[0]
print("del Heroes[0] :", Heroes)
Heroes.pop
print("Heroes.pop :", Heroes)
print("Heroes.index('슈퍼맨') : ",Heroes.index("슈퍼맨"))
print("each Hero!")
for hero in Heroes:
    print(hero)
Heroes.sort()
print("Heroes.sort() : ",Heroes)
