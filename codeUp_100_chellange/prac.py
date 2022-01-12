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

# n = int(input())
# num = [int(i) for i in input().split()]
#
# print(min(num))

# array_map = [[0 for i in range(19)] for j in range(19)]
#
# n = int(input())
#
# for i in range(n):
#     a, b = map(int, input().split())
#     array_map[a-1][b-1] = 1
#
# for i in range(19):
#     for j in range(19):
#         print(array_map[i][j], end=" ")
#     print()

# array_map = [[int(i) for i in input().split()] for j in range(19)]
#
# n = int(input())
#
# for i in range(n):
#     a, b = map(int, input().split())
#     for j in range(19):
#         array_map[a-1][j] = 0 if array_map[a-1][j] else 1
#
#     for k in range(19):
#         array_map[k][b-1] = 0 if array_map[k][b-1] else 1
#
# for i in range(19):
#     for j in range(19):
#         print(array_map[i][j], end=" ")
#     print()

# h, w = map(int, input().split())
# array_map = [[0 for i in range(w)] for j in range(h)]
# n = int(input())
#
# for i in range(n):
#     ln, d, x, y = map(int, input().split())
#     for j in range(ln):
#         if d:
#             array_map[x-1][y-1] = 1
#             x += 1
#         else:
#             array_map[x-1][y-1] = 1
#             y += 1
#
# for i in range(h):
#     for j in range(w):
#         print(array_map[i][j], end=" ")
#     print()

# ant_map = [[int(i) for i in input().split()] for _ in range(10)]
# start_x, start_y = 1, 1
# feed = 1
# status = [0, 0]
# ant_map[start_x][start_y] = 9
#
# while sum(status) != 2:
#     if ant_map[start_x][start_y+1] == 1:
#         status[0] = 1
#         if ant_map[start_x+1][start_y] == 1:
#             status[1] = 1
#         else:
#             if ant_map[start_x+1][start_y] == 2:
#                 start_x += 1
#                 ant_map[start_x][start_y] = 9
#                 break
#             status[1] = 0
#             start_x += 1
#             ant_map[start_x][start_y] = 9
#     else:
#         if ant_map[start_x][start_y+1] == 2:
#             start_y += 1
#             ant_map[start_x][start_y] = 9
#             break
#         status[0] = 0
#         start_y += 1
#         ant_map[start_x][start_y] = 9

# ant_map = [[int(i) for i in input().split()] for _ in range(10)]
# start_x, start_y = 1, 1
# x = 1
# y = 1
# while True:
#     if ant_map[x][y] == 0:
#         ant_map[x][y] = 9
#     elif ant_map[x][y] == 2:
#         ant_map[x][y] = 9
#         break
#
#     if (ant_map[x][y+1] == 1 and ant_map[x+1][y] == 1) \
#             or (x == 9 and y == 9):
#         break
#
#     if ant_map[x][y+1] != 1:
#         y += 1
#     elif ant_map[x+1][y] != 1:
#         x += 1
#
# for i in range(10):
#     for j in range(10):
#         print(ant_map[i][j], end=" ")
#     print()


# def find_feed(r, c):
#     global maze
#
#     if maze[r][c] == '2':
#         maze[r][c] = '9'
#         return
#
#     maze[r][c] = '9'
#
#     if c+1 < 10 and maze[r][c+1] == '0':
#         c += 1
#     elif not maze[r+1][c] == '1':
#         r += 1
#     else:
#         return
#
#     find_feed(r, c)
#
#
# maze = [list(input().split()) for _ in range(10)]
# find_feed(1, 1)
#
# for i in range(10):
#     for j in range(10):
#         print(int(maze[i][j]), end=' ')
#     print()

# def find_feed(r, c):
#     global maze
#
#     if maze[r][c] == '2':
#         maze[r][c] = '9'
#         return
#
#     maze[r][c] = '9'
#
#     if c+1 < 10 and maze[r][c+1] == '0' or maze[r][c+1] == '2':
#         c += 1
#     elif not maze[r+1][c] == '1' or maze[r+1][c] == '2':
#         r += 1
#     else:
#         return
#     find_feed(r, c)
#
#
# maze = [list(input().split()) for _ in range(10)]
# find_feed(1, 1)
#
# for i in range(10):
#     for j in range(10):
#         print(int(maze[i][j]), end=' ')
#     print()