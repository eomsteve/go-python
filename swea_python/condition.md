# 조건문

## if문

조건문은 True와 False를 반환한다.

True일 경우 명령문을 실행하고 반대의 경우 그냥 반환한다.

```python
# if 조건식 :
#   명령문
# 파이썬에서는 코드블록으로 구성해 기술해야하므로 명령문을 탭을통해 
# 한번 넣어주어야 한다.

score = 80
if score >= 40:
    print("합격입니다.!")

# score가 80점으로 40점보다 높으므로 결과는
# 합격입니다.! 가 나온다.

if score >= 40 : print("합격입니다.!")

#콜론 뒤에 작성해도 문제는 없지만 단순할경우에만 사용하는것이 좋다.
```

들여쓰기를 띄어쓰기 하나라도 잘못하게 되는순간 오류가 나타난다.

코드의 동일 수준에서의 동일 들여쓰기는 파이썬에서 아주 중요하다.

문장의 끝을 표시하는 `;` 생략가능 하지만 문장의 구분을 위해 사용할수 있다.

```python
#합격 혹은 불합격
result = "불합격입니다."
score = 50

if score >= 30:
    result = "합격입니다."
print(result)

#미리 변수에 결과를 저장한 뒤 조건문을 통과하게 되면 결과값이 바뀌도록 
#코드를 작성했다. result 변수가 미리 선언되지 않으면 오류가 나타난다.
```

## if~else

상호 배타적으로 조건을 수행하고자 할때 사용한다.

```python
# if 조건식 :
#   명령문
#   명령문
# else:
#   명령문

score = 80
if score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")
# 60점이 넘을경우 if문을 실행하고 60점이 넘지 못할경우 else문을 실행한다.
```

## if~elif~else

2개 이상의 다중 조건문을 사용할때 사용한다.

조건식 1, 조건식 2 ... 조건식 n

```python
# if 조건식 1:
#    명령문
# elif 조건식 2:
#   명령문
# else:
#   명령문
score = 70
if score >= 80:
    grade = "A"
elif score >= 60:
    grade = "B"
else:
    grade = "C"
# 여기서 조건문 종료
print(grade)
```
