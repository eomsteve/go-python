# 문제
# 팰린드롬은 앞으로 읽으나 뒤로 읽으나 똑같은 단어나 숫자들을 말한다. 일반적으로 대소문자를 구분하지 않지만, 공백은 구분한다.
#
# 다음은 팰린드롬의 예시이다.
#
# Anna
# Harrah
# Arora
# Nat tan
# 9998999
# 123 321
# $$$&&$$$
# 모든 라인에 대해 팰린드롬인지 아닌지를 구분하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 n이 주어진다.
#
# 각 테스트 케이스는 한 줄의 텍스트로 이루어져있으며, 비어있는 줄은 없다.
#
# 출력
# 각 테스트 케이스에 대해 정답을 출력한다.
#
# 팰린드롬일 경우 "Yes"를 출력하고, 그렇지 않을 경우 "No"를 출력한다.

# n = int(input())
# result = []
# for _ in range(n):
#     k = int(input())
#     str_list = [input() for _ in range(k)]
#
#     cnt = 0
#     for i in range(k):
#         for j in range(k):
#             if i == j:
#                 continue
#             is_pal1 = str_list[i] + str_list[j]
#             if is_pal1 == is_pal1[::-1]:
#                 result.append(is_pal1)
#                 cnt += 1
#                 break
#
#     if not cnt:
#         result.append(0)
#
# for i in range(n):
#     print(result[i])

# from itertools import combinations
#
# t= int(input())
# for _ in range(t):
#     k = int(input())
#     words = [input() for _ in range(k)]
#
#     combination = list(combinations(words, 2))
#     for a, b in combination:
#         tmp_a = a+b
#         tmp_b = b+a
#         if tmp_a == tmp_a[::-1]:
#             print(tmp_a)
#             break
#         if tmp_b == tmp_b[::-1]:
#             print(tmp_b)
#             break
#     else:
#         print(0)

n = int(input())
result = []
for _ in range(n):
    k = int(input())
    str_list = []
    for _ in range(k):
        str_list.append(input())

    cnt = 0
    for i in range(len(str_list)-1):
        for j in range(i + 1, len(str_list)):
            is_pal1 = str_list[i] + str_list[j]
            is_pal2 = str_list[j] + str_list[i]
            if is_pal1 == is_pal1[::-1]:
                result.append(is_pal1)
                cnt = 1
                break
            if is_pal2 == is_pal2[::-1]:
                result.append(is_pal2)
                cnt = 1
                break

    if not cnt:
        result.append(0)

for i in range(n):
    print(result[i])