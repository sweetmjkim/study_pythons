# 기본 구문
try :           # 콜론이 있다는건 영역이 있다는것이다.
    pass        # 업무 코드        # 문제발생이 되지않는다면 다음으로 진행된다.
except :
    pass        # 업무 코드 문제 발생 시 대처 코드
finally :
    pass        # try나 except이 끝난 후 무조건 실행 코드

# pure python with 계산기

# num_first = '4'
num_first = 4
num_second = 5
# 곱셈 연산

try :
    result = num_first / num_second
    pass        # 업무 코드
except :
    result = int(num_first) / int(num_second)
    pass        # 업무 코드 문제 발생 시 대처 코드
finally :
    pass        # try나 except이 끝난 후 무조건 실행 코드


print("{} = {} * {}".format(result, num_first, num_second))
pass