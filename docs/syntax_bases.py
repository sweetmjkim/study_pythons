# 코드 기본 형식
## import 시 주로 사용하는 방식
from classes_formats import person, Arithmetics, Class_name

# class basic format(기본 구조)
class Class_name:
    def __init__(self) :    # 생성자
        pass

    def function_name(self) :   # self 키워드 필요(class 소속 확인용)
        try :           # 콜론이 있다는건 영역이 있다는것이다.
            pass        # 업무 코드        # 문제발생이 되지않는다면 다음으로 진행된다.
        except :
            pass        # 업무 코드 문제 발생 시 대처 코드
        finally :
            pass        # try나 except이 끝난 후 무조건 실행 코드
        return 0
    
# 기본 function 형식 - 기다림. 불리울 때 기능한다. def function () : -> tap pass -> return 0
def function_name() : 
    try :           # 콜론이 있다는건 영역이 있다는것이다.
        pass        # 업무 코드        # 문제발생이 되지않는다면 다음으로 진행된다.
    except :
        pass        # 업무 코드 문제 발생 시 대처 코드
    finally :
        pass        # try나 except이 끝난 후 무조건 실행 코드
    return 0

if __name__ == "__main__" :
    try :           # 콜론이 있다는건 영역이 있다는것이다.
        pass        # 업무 코드        # 문제발생이 되지않는다면 다음으로 진행된다.
    except :
        pass        # 업무 코드 문제 발생 시 대처 코드
    finally :
        pass        # try나 except이 끝난 후 무조건 실행 코드

