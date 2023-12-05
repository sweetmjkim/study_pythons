# 구구단 5단 단계별 표시
# 예. 5 * 1 = 5
#     5 * 2 = 10
#      ....
#     5 * 9 = 45

# option) 단수 입력 받아 연산

num_timestable = 5 # 구구단 단수
num_number = 0
while num_number < 9 :
    pass
    num_number = num_number + 1
    result = num_timestable * num_number
    print("{} * {} = {}".format(int(num_timestable), int(num_number), int(result)))
    pass
print("구구단 5단 완성!")