#-*-coding:CP949-*-

"""
import pickle
gameOption = {
    "Sound":8,
    "VideoQuality":"HIGH",
    "Money":100000,
    "WeaponList":["gun","missile","knife"]
}

file = open("saved.txt","wb")
pickle.dump(gameOption,file)
print("피클링된 데이터 생성 완료")
file.close()
"""
import pickle
file=open("saved.txt","rb")
obj = pickle.load(file)
print(obj)
file.close()