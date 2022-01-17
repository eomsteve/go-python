# 회문 확인하기
# 제약조건 : 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

# string_01 = "A man, a plan a canal: Panama"
string_01 = "race a car"
result = []

for i in string_01:
    if i.isalpha():
        result.append(i.lower())

# print(result)
j = len(result) // 2
# print(result[-1:j:-1])
# print(result[:j])

if result[:j] == result[-1:j:-1]:
    print(True)
else:
    print(False)

    # string = "race a car"
# j = len(list(string))/2
# j = int(j)
# if string[:j] == string[-j:]:
#     print(True)
# else:
#     print(False)
