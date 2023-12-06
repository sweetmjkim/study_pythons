# 변수 선언 후 정의 시 고려점(넣는 값이 문자 or 숫자)
# 문자 출력
print("hello, world! myung jun kim.") # 상수(값을 직접 전달하는 방식. 왠만하면 사용하지말아야한다.)

helloworld = "hello, world! myung jun kim." # 문자형 변수 # ""로 표시 해줘야한다.
print(helloworld)

# 숫자 합산 출력
numbers = 3 + 5 # 숫자형 변수
print(numbers)

# 데이터 타입 : 문자형 or 숫자형 등 변수에 대한 정의


# 가정문
if 5 > 2:
    print("Five is greater than two!")

# 가정문1
print(numbers)

if 5 > 2: # 묶음 기호인 : 과 tab은 하나에 쌍
    pass # 디버깅할때 유용하다. pass문 : 아무 동작은 하지않지만 나중에 코드 추가 및 구조를 확인 할때 사용하는 빈 문장 
    print("Five is greater than two!")
    print("end")

# 한줄에 출력
first = "First"
second = "Second"
print("first : {}".format(first), end=", 다음 줄 ")
print("second : {}".format(second))
print("End progrem!")