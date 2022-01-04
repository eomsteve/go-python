# #1
# T = float(input())
# inch = T
# result = 2.54 * inch
# #print("{0:.2f} inch => {1:.2f} cm".format(inch,result))
#


#if

# num = int(input())
# cnt = 0
# for i in range(1,num + 1):
#     if num % i == 0:
#         print(f"{i}(은)는 {num}의 약수입니다.")
#         cnt += 1
# if cnt == 2:
#     print(f"{num}(은)는 1과 {num}로만 나눌 수 있는 소수입니다.")
#
# al = input()
# result = ord(al)
# if result >= 97:
#     print(f"{al} 는 소문자 입니다.")

# for
#
# for i in range (1, 101):
#     print(i)

#make fibo
#
#
# num = int(input())
#
# def factorial(num):
#     if(num == 1) : return 1
#     return num * factorial(num-1)
# print(factorial(num))

test_list = [2, 4, 6, 8, 10]

num = 10

def find_at_list(num, ls):
    for i in ls:
        if( i == num):
            return print(f"{num} => True")
        else:
            none = 1
    if none == 1:
        return print(f"{num} => False")


find_at_list(num, test_list)