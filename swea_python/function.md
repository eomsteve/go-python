# 함수

효율적이고 구조화된 프로그램 생성

프로그램에서 어떤 특정 기능을 수행할 목적으로
만들어진 재사용 구조의 코드 부분

하나의 큰 프로그램을 여러부분으로 나눌 수있기 때문에 구조적
프로그래밍이 가능해짐

필요할때마다 호출

수정이 용이함

* 순수함수 : 결과값 반환외에 외부에 영향을 주지않는 함수

함수형 프로그래밍 지원에서는 순수 함수를 인자
반환값으로 사용함

함수의 호출

`print()` : 괄호 안에 인자를 전달하는데
 인자가 출력되로록 하는 함수이다.

## 함수의 선언

```python
def function_name (parameter):
    #명령믄
    return parameter
```

## 함수의 유형

1. 매개변수와 반환값이 있는 함수
2. 매개변수는 없고 반환값이 있는 함수
3. 매개변수는 있고 반환값이 없는 함수
4. 매개변수와 반환값이 없는 함수

## 함수와 매개변수

함수 호출시 입력값을 전달받기 위한 함수

전달받은 인자의 값에 의해 결정됨

선언된 매개변수의 개수만큼 인자 전달 가능

#### 매개변수와 개수 불일치 문제

일치할 경우 문제없이 원하는 결과를 받을 수 있다.

인자값이 불이치할경우 타입에러가 나타난다.
오류 메세지는 함수 호출시 전달되지 않은 인자가
존재한다는 말을 하고 종료된다. 더 많은
인자를 전달할 경우 몇개의 인자를 더 전달했다는
오류문구를 출력한다.

## 언팩 연산자 (`*`)

파라미터의 개수를 가변적으로 사용가능

```python
def cal_sum(*params):
    total = 0
    for val in params:
        total += val
    return total

ret_val = cal_sum(1, 2)
```

가변형 매개변수는 인자들이 튜플 형식으로 입력받게 된다.

가변형 매개변수를 가장 마지막 매개변수로 해야 
부작용 없이 사용할 수 있다.

```python
def calc_sum(precision,*params):
    if precision == 0:
        total = 0
    elif 0 < precision < 1:
        total = 0.0
    for val in params:
        total += val
    return total

ret_val = calc_sum(0, 1, 2) # 3반환
```

언팩 연산자를 사용하면 함수는 여러개의 값을 반환할 수 있다.

```python
def calc_sum(precision,precision2,*params):
    if precision == 0:
        total1 = 0
    elif 0 < precision < 1:
        total1 = 0.0
    if precision2 == 0:
        total2 = 0
    elif 0 < precision2 < 1:
        total2 = 0.0
    for val in params:
        total1 += val
        total2 += val
    return total1, total2

ret_val = calc_sum(0, 1, 2) 
# 튜플을 반환해서 하나 이상의 값을 반환할 수 있다.
ret_val = calc_sum(0, 0.1 , 1, 2)
```

## 키워드 언팩 연산자 (`**`)

매개변수의 개수를 가변적으로 사용할 수있도록 한다.
키워드 인자들을 전달해 매개변수를 딕셔너리 형식으로
처리한다.

```python
def use_keyword_arg_unpacking(**params):
    for k in params.key():
        print("{0}: {1}.format(k, params[k]")
```

### 기본값을 갖는 매개변수

매개변수 인자값이 생략?

```python
def calc(x, y, operator="+"):
    if operator == "+":
        return x+y
    else:
        return x-y
# 3번째 인자는 안들어와도 기본값으로 덧샘을 한다.
```

## 스코프

지역변수, 전역변수의 개념 

### 변수에 접근하는 절차

1. 함수 스코프 내에서 가장먼저 변수를 찾는다
2. 전역스코프에서 변수를 찾는다. (함수내에 변수가 없을경우)

그렇다면 전역변수와 지역변수를 동시에 호출하면?

```python
def change_global_var():
    global x
    x+=1
# global키워드를 통해 x에 접근, 값을 증가시킴
x = 5 
change_global_var()
print(x) #전역변수의 값 6
```

## 고급함수 사용법

### 중첩함수

함수 내에 중첩함수를 선언해 사용 가능
 
1. 중첩함수를 포함하는 함수 내에서만 호출이 가능함
2. 충첩함수를 포함하는 함수의 스코프에도 접근이 가능함

프로그램의 유연성을 높이기 위해 함수를 매개변수로 전달하는
방식 선호

### 람다식

매번 함수를 선언해서 사용하기 어렵기떄문에 람다식 사용

`Lambda 매개변수 : 반환값`

1. 변수에 저장해 재사용이 가능한 함수처럼 사용함
2. 기존의 함수처럼 매개변수의 인자로 전달함

### 클로저

1. 중첩함수에서 중첩함수를 포함하는 함수의 scope에 접근가능
2. 정보은닉구현
3. 저역변수 남용방지
4. 우아한 구조

```python
def outer_fn():
    id = 0
    
    def inner_fn():
        nonlocal id
        id  +=1
        return id
    return inner_fn()

mk_id = outer_fn()
```
