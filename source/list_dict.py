#-*-coding:CP949-*-

"""
Heroes = []
Heroes.append("���̾��")
Heroes.append("���� ��Ʈ������")
print(Heroes)

letters = ["A","B","C","D","E","F"]
print(letters[-3:-1])
print(letters[0:])
print(letters[:])
print(letters[:-2])

"""

Heroes = ["���̾��","�丣","��ũ","��Į�� ��ġ"]
Heroes[2] = "�����̴���"
Heroes.append("���۸�")
Heroes.insert(0,"��Ʈ��")
Heroes.insert(3,"�������")

Heroes.remove("��Į�� ��ġ")

#if "�丣" in Heroes:
#    Heroes.remove("�丣")


del Heroes[0]
print("del Heroes[0] :", Heroes)
Heroes.pop
print("Heroes.pop :", Heroes)
print("Heroes.index('���۸�') : ",Heroes.index("���۸�"))
print("each Hero!")
for hero in Heroes:
    print(hero)
Heroes.sort()
print("Heroes.sort() : ",Heroes)
