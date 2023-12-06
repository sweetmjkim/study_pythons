## for 기본 문형
for X in [] :
    pass

# 얼마만큼 반복할지에 대한 값들을 알려줌
numerics = 0
numerics = [0, 1, 2, 3, 4]    # 5개수 값으로 이루어진 리스트
# for 순서있는값 in 리스트변수 :
#     pass

for number in numerics :
    pass
    print(number)

# 문자 3개 값들로 이루어진 리스트
for str_fruit in ["apple", "melon", "banana", "cherry"] :    # 반복 대상 리스트 직접 넣기
    pass
    print("furit name : {}!".format(str_fruit))


list_fruits = ["apple", "banana", "cherry"]
for str_fruit in list_fruits :    # 반복 대상 리스트 직접 넣기
    pass
    print("furit name : {}!".format(str_fruit))


numerics = [0, 1, 2, 3, 4]    # 5개수 값으로 이루어진 리스트
for number in numerics :
    pass
    print("number : {}.". format(number+2))
print("End Program!")