for i in [] :
    print
    
number = 0
marks = [90, 25, 67, 45, 80]   
for mark in marks :
    number = number +1
    if mark >= 60 :
        print("{}번 학생은 합격입니다.".format(number))
    else :
        print("{}번 학생은 불합격입니다.".format(number))
    