# input() 대한 기본 사항
# str_start = "start, programming."
# print("{}".format(str_start)) # 출력 :
# input() # 입력
# pass # 종료

# print("-----------------------------------------------------------------------------------")

# str_start = "start, programming."
# print("{}".format(str_start)) # 출력
# str_input_desc = "영문이름 입력 : "
# str_input = input("{}".format(str_input_desc)) # 입력된 정보를 디버깅에서 확인 하고자 할때 
# pass # 종료

# print("-----------------------------------------------------------------------------------")

# # input() 대한 숫자 받아 환산 하기
# # 풀기 : 출생연도 입력 받아 나이 계산 
# # 예. 2023(올해) - 2000(출생년도) = 21
str_start = "start, programming."
print("{}".format(str_start)) # 출력
str_input_desc = "출생년도 입력 : "
num_input_birthyear = input("{}".format(str_input_desc)) # 입력
num_age = 2023 - int(num_input_birthyear)
print("출생년도 기준 내 나이 계산 : {}살".format(num_age))

#3 4
pass # 종료