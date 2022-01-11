# s = input()
#
# for i in range(0, len(s), 2):
#     print(s[i:i+2], end=" ")


# t = input().split(":")
#
# print(t[1])

# a, b, c = input().split(" ")
# a = int(a)
# b = int(b)
# c = int(c)
#
# print(a+b+c, end=" ")
# print(f"{(a+b+c)/3:.2f}")

# a = [int(x) for x in input().split(" ")]
#
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# n = int(input())
#
# n = bool(n)
#
# print(not n)

# n = int(input())
# print(~n)

# n = input()
#
# if n == 'A':
#     print('best!!!')
# elif n == 'B':
#     print('good!!')
# elif n == 'C':
#     print('run!')
# elif n == 'D':
#     print('slowly~')
# else:
#     print("what?")

# n = int(input())
#
# if n//3 ==1:
#     print("spring")
# elif n//3 == 2 :
#     print("summer")
# elif n//3 == 3 :
#     print("fall")
# else:
#     print("winter")

# n = int(input())
# start, result = 0, 0
#
# while start != n + 1:
#     if start % 2 == 0:
#         result += start
#     start += 1
#
# print(result)
# n = int(input())
# s = 0
# i = 0
# while s < n:
#     s += i
#     i += 1
#
# print(s)

# n = int(input(), 16)
#
# for i in range(1, 16):
#     print(f"{n:X}*{i:X}={(i*n):X}")

# n = int(input())
#
# for i in range(1, n+1):
#     count = sum([1 for j in str(i) if j in '369'])
#     print('X' if count else i, end=' ')
#
# r, g, b = map(int, input().split(" "))
# cnt = 0
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print(i, j, k)
#             cnt += 1
#
# print(cnt)

# h, b, c = map(int, input().split(" "))
#
# result = h * b * c
# result /= 8
# result /= 1024
# result /= 1024
# print(f'{result:.2f} MB')

# n = int(input())
#
# for i in range(1, n+1):
#     if i % 3 == 0:
#         print(end='')
#     else:
#         print(i, end=" ")

# a, b, c = map(int, input().split())
# d = 1
# while d%a!=0 or d%b!=0 or d%c!=0 :
#     d+=1
# print(d)
#
# n = input()
# ln = [0 for i in range(23)]
#
# num = [int(i) for i in input().split()]
#
# for i in range(1, 24):
#     ln[i-1] = num.count(i)
#
# for i in range(len(ln)):
#     print(ln[i], end=" ")

# n = int(input())
# num = [int(i) for i in input().split()]
# num.reverse()
# print(num)

n = int(input())
num = [int(i) for i in input().split()]

print(min(num))