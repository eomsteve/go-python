# 로그파일 재정렬

# 로그를 재 정렬 하라. 기준은 다음과 같다.
# 1. 로그의 가장 앞 부분은 식별자다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.

# 입력

logs = ["dig1 8 1 5 1", "zet1 art zerA", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

# 2. 문자로 구성된 로그와 숫자로 구성된 로그를 찾아 정렬해야한다.
# 3. 식별자는 처음 순서에 영향을 끼치지 않지만 로그의 비교 부분이 동일한 문자일 경우 식별자의 순서로 우선순위를 정한다.
# 4. 숫자 로그는 크기에 상관 없이 입력된 순서대로 한다.

# solve : 문자로그 리스트와 숫자로그 리스트로 나누어 두번째 값만 비교해 정렬 시도
# - 문자로그 비교시 같은값이 나오면 앞의 식별자로 우선순위를 정함

letter = []
numbers = []

for log in logs:
    if log.split()[1].isalpha():
        letter.append(log)
    else:
        numbers.append(log)
# test = ["art zero","own kit dig","banana coke","ary zero"]
# print(sorted(test))
#
# print("art zero kk".split()[1:])
print(letter)
print(letter[2].split()[1:])
letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
print(letter)