# 해시

# 문제

해싱을 하는 공식을 만들어 문제를 푼다.

# 배운것

오버플로우가 날 경우를 대비해야한다. 즉 큰수가 들어왔을때 온전한 결과를
도출할 수 없다. 따라서 마지막에 M으로 나누긴 하지만 중간중간 M보다 클 경우
M으로 나눈 나머지를 더해도 문제가 없다.


```python
# 50점 짜리

n = int(input())
word = input()
r = 31
M = 1234567891
alpha = {chr(a): a-96 for a in range(ord('a'), ord('z')+1)}

total = 0
for i in range(n):
    total += (alpha[word[i]] * r ** i) % M

print(total)
```

```python
# 100점짜리
n = int(input())
word = input()
r = 31
M = 1234567891
alpha = {chr(a): a-96 for a in range(ord('a'), ord('z')+1)}

total = 0
for i in range(n):
    total += (alpha[word[i]] * r ** i) % M
    #  total의 값을 계속 M으로 나누어서 오버플로우를 방지한다.
    if total > M:
        total %= M

print(total)
```