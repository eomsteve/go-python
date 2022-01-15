# 1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아
#
# 콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.

# num = list(range(1, 201))
#
# for i in num:
#     if (i % 7 == 0) and (i % 5 != 0):
#         if i == 196:
#             print(i)
#             break
#         print(i, end=",")

# 100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분해 출력 하는 프로그램을 작성하십시오.

# num = list(range(100, 301))
#
# for i in num:
#     if ((i // 100) % 2 == 0) and ((i // 10) % 2 == 0) and (i % 2 == 0):
#         if i == 288:
#             print(i)
#             break
#         else:
#             print(i, end=',')

# 다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,
#
# 60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.

# grade = {"1": 88, "2": 30, "3": 61, "4": 55, "5": 95}
#
# for i, j in grade.items():
#     if j >= 60:
#         print(f'{i}번 학생은 {j}점으로 합격입니다.')
#     else:
#         print(f'{i}번 학생은 {j}점으로 불합격입니다.')

# result = 0
# for i in range(1, 101):
#     if i % 3 == 0:
#         result += i
#
# print(f'1부터 100사이의 숫자 중 3의 배수의 총합: {result}')

# blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# b_type = ['A', 'O', 'B', 'AB']
# cnt = []
# for i in b_type:
#     cnt.append(blood.count(i))
#
# result = dict(zip(b_type, cnt))
#
# print(result)

# std = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# result = 0
#
# while std:
#     i = std.pop()
#     if i >= 80:
#         result += i
#
# print(result)

# x = 5
# while x:
#     j = 0
#     while j != x:
#         print("*", end="")
#         j += 1
#     print()
#     x -= 1

# i = int(input())
#
# print(f'{i:b}')

# 다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.

# num = int(input())
# list_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# count = [0 for _ in range(10)]
# while num:
#     count[num % 10] += 1
#     num //= 10
#
# for i in range(10):
#     print(list_num[i], end=" ")
# print()
# for i in range(10):
#     print(count[i], end=" ")

# input_str = list(input())
# j = len(input_str)//2
# print("".join(input_str ))
# if input_str[-j:] == input_str[0:j]:
#     print("입력하신 단어는 회문(Palindrome)입니다.")

# 다음의 결과와 같이 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.
#
# n = int(input())

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# for i in range(1, num+1):
#     result.append(fib(i))

# fibList = []
#
# def fib(n):
#     fibList=[1, 1]
#     if n==1 or n==2:
#         return 1
#     for i in range(2,n):
#         fibList.append( fibList[i-1] + fibList[i-2] )
#     return fibList
#
# fib(10)
#
# print(fib(10))

# numbers = list(map(int, input().split(",")))
#
#
# def my_pow(n):
#     return n ** 2
#
#
# for i in numbers:
#     print(f'square({i}) => {my_pow(i)}')

#람다 마스터

# num = [int(i) for i in range(1, 11)]
#
# result = list(filter(lambda i: i % 2 == 0, list(map(lambda i: i ** 2, num))))
#
# print(result)