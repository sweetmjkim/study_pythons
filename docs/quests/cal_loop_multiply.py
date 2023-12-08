# 사용자 입력 반복 곱셈 계산기
# 'q' 입력 시 종료
# 최소 function 1개 사용
# 실행 이미지 링크 공유(최소 2회 계산)

# def multiply() : 
#     num_first = int(input("첫번째 입력값 : "))
#     num_second = int(input("두번째 입력값 : "))
#     result = num_first * num_second
#     return result
# num_multiply = multiply()
# print("first * second = {}" .format(num_multiply))
# print("-------------------------------------------------------------------------")

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
