# input(두 값은 정수) : 몸무게, 키
# BMI = 몸무게(kg) / 키(m)^2
# BMI 분류
# 18 미만 : 저체충
# 18 -22 : 정상
# 23-24 : 과체중
# 25 이상 : 비만

str_weight = int(input("몸무게(kg)"))
str_height_CM = int(input("키(cm)"))
str_height_M = str_height_CM/100

BMI = str_weight/(str_height_M**2)
print(int(BMI))

BMI
if BMI >= 25 :
    print("{}은 비만이다.".format(int(BMI)))
elif BMI > 22 : 
    print("{}은 과체중이다.".format(int(BMI)))
elif BMI > 18 : 
    print("{}은 정상이다.".format(int(BMI)))
else : 
    print("{}은 저체중이다.".format(int(BMI)))