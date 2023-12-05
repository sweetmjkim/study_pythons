# input(두 값은 정수) : 몸무게, 키
# BMI = 몸무게(kg) / 키(m)^2
# BMI 분류
# 18 미만 : 저체충
# 18 -22 : 정상
# 23-24 : 과체중
# 25 이상 : 비만

str_name = input("이름")
str_weight = int(input("몸무게(kg)"))
str_height_CM = int(input("키(cm)"))
str_height_M = str_height_CM/100

BMI = str_weight/(str_height_M**2)
print(int(BMI))

BMI
if BMI >= 25 :
    print("{}님에 BMI 결과 {}로 비만입니다.".format(str_name, (int(BMI))))
elif BMI >= 23 : 
    print("{}님에 BMI 결과 {}로 과체중입니다.".format(str_name, (int(BMI))))
elif BMI >= 18 : 
    print("{}님에 BMI 결과 {}로 정상입니다.".format(str_name, (int(BMI))))
else : 
    print("{}님에 BMI 결과 {}로 저체중입니다.".format(str_name, (int(BMI))))
