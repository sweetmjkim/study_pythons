# class Arithemtic : 곱셈, 나눗셈 추가
#뺄셈, 곱셈, 나눗셈 실행

class Arithmetic:
    def __init__(self) :    # 생성자
        pass

    def minus(self, first, second) : 
        result = first - second
        return result

    def multiply(self, first, second) :   
        sum = first * second
        return sum
    
    def division(self, first, second) :   # self 키워드 필요(class 소속 확인용)
        sum = first / second
        return sum

arithmetics = Arithmetic()
print(arithmetics.minus(10, 5))
print(arithmetics.multiply(10, 5))
print(arithmetics.division(10, 5))