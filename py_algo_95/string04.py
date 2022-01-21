# babad

my_input = input()

# 생각 1 : 전체 문자열을 돌면서 팰린드롬을 찾아본다  팰린드롬 판별 함수를 만든다.


def is_paln(word):
    if word == word[::-1]:
        return word
    else:
        return ""


result = ""
if len(my_input) <= 1:
    result = my_input

for i in range(len(my_input)):
    for j in range(len(my_input) - i + 1):
        if i == 0:
            pal_result = is_paln(my_input[j:])
        else:
            pal_result = is_paln(my_input[j:-i])
        if len(pal_result) > len(result):
            result = pal_result

print(len(result))

# 55분 소요, 문자열안의 문자열을 도는법에 대해 너무 오래 생각했다. j:j+i 이걸 생각하는데 오래걸림
# ERROR : 모든 문자열이 팰린드롬일때 판별이 안된다.
# 문자열이 1보다 작을 경우 예외처리 추가, j+i는 1보다 작은 예외처리를 아에 안하기 위해 2부터 시작했기 때문에
# 만들어진 예외임으로 큰 반복문의 i값을 0부터 시작시켰다. 이로서 모든 문자열도 확인할 수 있을 줄 알았으나
# j:-0 = j:0 아무것도 안나타나기 때문에 예외 처리 추가
# 만약 문자열 전체가 팰린드롬인지 판단해야할 때를 위해서 i값이 0이면 전부를 보는 분기문 추가
# 시간초과.... 결과는 나온다 반쪽승리


def long(words):
    def expand(left, right):
        while left >= 0 and right <len(words) and words[left] == words[right]:
            left -= 1
            right +=1
        return words[left+1 : right]
    if len(words) < 2 or words == words[::-1]:
        return len(words)
    result = ''
    for i in range(len(words) - 1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    return len(result)

n = input()

print(long(n))

