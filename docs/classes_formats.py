# class 사용 순서
# 1. inport : 같은 파일에 있을 경우 생략.
# 2. class instance : 생성자 호출
# 3. call function : 원하는 function 호출

# class basic format(기본 구조)
class Class_name:
    def __init__(self) :    # 생성자
        pass

    def function_name(self) :   # self 키워드 필요(class 소속 확인용)
        pass
        return 0

class Person:
    def add_age(self) :
        pass
        print("45세")
        return 0

# 1. inport : 같은 파일에 있을 경우 생략.
# 2. class instance
person = Person()
# 3. call function  
person.add_age()

# 사칙연산 되는 class 작성
# 덧셈, 뺄셈
class Arithmetics:
    def __init__(self) :    # 생성자(class 갖고 있는 자원)
        pass                # 이단계가 되면 내부적으로 기술되어있음.(모든자원을 반납해라는 의미가 숨겨져있음.)

    def add(self, first, second) : # 호출시 변수에 값이 활당됨.
        sum = first + second    #상수값을 쓰지않는다. 변수값을 넣는다.
        # return = 0
        return sum # 상수 대신 변수 사용

    def minus(self, first, second) : 
        result = first - second
        return result
    
# 1. inport : 같은 파일에 있을 경우 생략.
# 2. class instance
arithmetics = Arithmetics()
# 3. call function
print(arithmetics.add(5, 6))
pass