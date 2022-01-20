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

# n = int(input())
# result = []
# for _ in range(n):
#     k = int(input())
#     str_list = []
#     for _ in range(k):
#         str_list.append(input())
#
#     cnt = 0
#     for i in range(len(str_list)-1):
#         for j in range(i + 1, len(str_list)):
#             is_pal1 = str_list[i] + str_list[j]
#             is_pal2 = str_list[j] + str_list[i]
#             if is_pal1 == is_pal1[::-1]:
#                 result.append(is_pal1)
#                 cnt = 1
#                 break
#             if is_pal2 == is_pal2[::-1]:
#                 result.append(is_pal2)
#                 cnt = 1
#                 break
#
#     if not cnt:
#         result.append(0)
#
# for i in range(n):
#     print(result[i])

# def get_strong_word(words_x, words_y):
#     number_x = number_y = 0
#     for word_x in words_x:
#         number_x +=ord(word_x)
#     for word_y in words_y:
#         number_y +=ord(word_y)
#     return words_x if number_x > number_y else words_y
#
# print(get_strong_word('z','a'))
# print(get_strong_word('tom','john'))

# 모든 부분집합 : 멱집합
# [1,2,3] >> 1 2 3 12 13 23 123 ''
# [0, 0, 0] : selected 각 요소가 부분집합에 포함되는지 여부를 표시하는 배열
# idx : 포함여부 결정할 요소 인덱스

# N = 3
# arr = [1, 2, 3]
# selected = [0, 0 ,0]
#
#
# def ps(idx):
#     if idx == N:  # 모든 요소의 포함여부 결정, 인덱스 벗어남
#         for i in range(N):
#             if selected[i]:
#                 print(arr[i],end="")
#         print()
#         return
#     selected[idx] = 1 # idx 번째 요소가 부분집합에 포함
#     ps(idx + 1)
#     selected[idx] = 0 # idx 번째 요소가 부분집합에 미포함
#     ps(idx + 1)

# def is_pal_recursive(word):
#     if type(word) is str:
#         word_list = list(word)
#     else:
#         word_list = word
#     if len(word) == 1:
#         return
#     if word_list.pop() == word[0]:
#         print(word_list, word[0])
#         return is_pal_recursive(word_list)
#     else:
#         return print("hjo")
#
# print(is_pal_recursive('tomato'))
# print(is_pal_recursive('racecar'))
# print(is_pal_recursive('azza'))

# def is_pal_recursive2(word):
#     if len(word) <= 1:
#         return True
#     if word[0] == word[-1]:
#         return is_pal_recursive2(word[1:-1])
#     else:
#         return False

# def is_pal_recursive(word):
#     if type(word) is str:
#         word_list = list(word)
#     else:
#         word_list = word
#     if len(word) <= 1:
#         return True
#     if word_list.pop() == word_list.pop(0):
#         return is_pal_recursive(word_list)
#     else:
#         return

a = ['cde', 'cfc', 'abz']

print(sorted(a, key=lambda s: (s[0], s[-1])))
