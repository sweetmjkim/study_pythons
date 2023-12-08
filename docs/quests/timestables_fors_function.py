# 30, 35, 20 단 대한 출력
# timestables_fors.py -> function 화
# option) [30, 35, 20] 부분 사용자 입력, 'q'이면 종료


# timestables_fors.py 예제
# num_timestable = 5 # 구구단 단수
# num_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number in num_number :
#     result = number * num_timestable
#     pass
#     print("{}*{} = {}".format(num_timestable, number, result))
# print("구구단 5단 완성!")

미완성

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def num_number() : 
    num_timestable = int(input())
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = num_timestable * num_list
    return result
num_number = num_number()
print("first * second = {}" .format(num_number))
print("-------------------------------------------------------------------------")

while True :
        num_multiply = input("종료를 원하면 'q'키 / 계속 진행은 Enter키 누르세요.")
        if num_multiply == 'q' :
             print("곱셈용 계산기 종료!")
             break
        else : 
            num_first = int(input("첫번째 입력값 : "))
            num_second = int(input("두번째 입력값 : "))
        result = num_first * num_second
        print("first * second = {}" .format(result))
        print("-------------------------------------------------------------------------")










    num_number = ()
    number = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    result = number * num_timestable
    pass
    print("{}*{} = 구구단{}단 완성".format(num_timestable, num_number, result))
    return result
num_number = num_number()


# def multiply() : 
#     num_first = int(input("첫번째 입력값 : "))
#     num_second = int(input("두번째 입력값 : "))
#     result = num_first * num_second
#     return result
# num_multiply = multiply()
# print("first * second = {}" .format(num_multiply))