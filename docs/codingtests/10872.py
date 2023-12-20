# 팩토리얼
# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.
# 출력
# 첫째 줄에 N!을 출력한다.

# N = 0

# for i in [] :
#     pass

# if True :
#     print
# elif True :
#     N >= 12
#     print
# else :
#     print


# n = 10
# count = 0
# N = []
# while count <= int(n) :
#     count += 1
#     N.append(count)
#     pass
#     for i in range(n):
#         i = i*1
# print(N)



# num_repeat = int(input())                                       # 1. 계산할 값(N) 입력
# a = 0                                       
# b = 1                                                           # 2. for 문을 시작하기 전에 기본값(1)을 설정
# for i in range(num_repeat):                                     # 3. 1부터 N까지 계속 곱하는 반복문 필요    -> for i in range(num_repeat):
#     a = a + 1                                                   # 4. 반복문이 진행될수록 곱할 값은 1이 증가
#     b = b*a                                                     # 5. 곱셈 진행
#     pass
# print(b)  


class Fcalculator:
    def __init__(self, n):
        self.n = n
    def factorial(self):
        if self.n == 0 or self.n == 1:
            return 1
        else:
            return self.n * Fcalculator(self.n-1).factorial()  
number = int(input("계산하고 싶은 숫자를 입력해 주세요: "))
calculator = Fcalculator(number)
result = calculator.factorial()
print ("{}! = {}".format(number,result))

