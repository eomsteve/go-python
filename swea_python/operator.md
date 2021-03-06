# 연산자

연산자는 프로그래밍 로직을 위해 필수적인 요소이다.

## 산술 대입 연산자

* `+` 더하기
* `-` 빼기
* `*` 곱하기
* `/` 나누기 (부동 소수점 숫자 결과 반환)
* `//` 몫
* `%` 나머지
* `**` 제곱

### 산술 연산자 우선순위
* 괄호`()` 우선순위가 가장 높다.

### 문자형과 숫자형 연산

문자열끼리는문자열 덧샘시 접합 연산이되어 `+`연산자를 사용가능하다.

각기 다른 자료형과의 연산은 타입에러가 발생한다.
이를방지하기위해 형변환 함수 `int()`, `string()`등을 이용해
자료형을 일치시킨후 계산한다.

## 대입 연산자

* `=` 대입(할당)
* `+=` 좌변의 변수에서 우변의 값을 더해 좌변의 변수에 대입
* `-+` 좌변의 변수에서 우변의 값을 빼서 좌변의 변수에 대입
* `*=` 좌변의 변수에서 우변의 값을 곱해 좌변의 변수에 대입
* `/=` 좌변의 변수에서 우변의 값을 나눠 좌변의 변수에 대입 
* `//=` 좌변의 변수를 우변의 값을 나눈 볷을 좌변의 변수에 대입
* `%=` 좌변의 변수를 우변의 값으로 나눈 나머지를 죄변의 변수에 대입
* `**=` 좌변의 변수를 우변의 값으로 제곱해서 좌변의 변수에 대입

## 관계 연산자

* `==` 양변의 값을 비교 같으면 참
* `!=` 양변의 값이 다르면 참
* `>` 좌변의 값이 우변의 값보다 크면 참
* `<` 좌변의 값이 우변의 값보다 작으면 참
* `>=` 좌변의 값이 우변의 값보다 크거나 같으면 참
* `<=` 좌변의 값이 우변의 값보다 작거나 같으면 참

## 논리연산자

* `and` 양변의 값 모두 참일경우 True 반환
* `or` 양변의 값 모두 거짓일 경우 False 반환
* `not` 참 혹은 거짓을 반대로

## 비트 연산자

코드를 작성하면서 비트 기반의 연산이 필요할 경우가 있다.

* `&` 양변의 비트값 모두 1일 경우에만 1 반환
* `|` 양변의 값 모두 0일경우에만 0반환
* `^` 양변의 값이 다를경우 1, 같을경우 0 반환
* `~` 비트값이 1일경우0, 0일경우 1 반환
* `<<` 좌변의 값을 우변의 값만큼 비트를 왼쪽으로 이동
* `>>` 좌변의 값을 부면의 값만큼 비트를 오른쪽으로 이동