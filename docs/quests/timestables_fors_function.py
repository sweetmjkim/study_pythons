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

def timestable():
    while True:
        num_multiply = input("구구단 숫자(20, 30, 35) 중 입력하거나 종료를 원하면 'q'를 입력하세요.")
        if num_multiply == 'q':
            break
        num_multiply = int(num_multiply)
        for num_list in range(1, 10):
            print("{} * {} = {}".format(num_multiply, num_list, num_multiply * num_list))
timestable()