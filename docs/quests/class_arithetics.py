# class Arithemtic : 곱셈, 나눗셈 추가
#뺄셈, 곱셈, 나눗셈 실행

class Arithmetic:
    def __init__(self) :    # 생성자
        pass
    
    def add(self, first, second) :
        add_result = first + second
        return add_result

    def minus(self, first, second) : 
        minus_result = first - second
        return minus_result

    def multiply(self, first, second) :   
        multiply_result = first * second
        return multiply_result
    
    def division(self, first, second) : 
        division_result = first / second 
        return division_result

first1 = int(input("첫번째 : "))
second2 = int(input("두번째 : "))
arithmetics = Arithmetic()
print("{}" .format(arithmetics.add(first1, second2)))
print("{}" .format(arithmetics.minus(first1, second2)))
print("{}" .format(arithmetics.multiply(first1, second2)))
print("{}" .format(arithmetics.division(first1, second2)))
num_A,num_B = map(int, input().split())