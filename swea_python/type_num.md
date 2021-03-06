# 리터럴

* 정수형 리터럴
  * 15
* 부동솟숫점 숫자형 리터럴
  * 3.14
* 문자열 리터럴
  * '파이썬'
* 부울형 리터럴
  * True, False
* 리스트형 리터럴
  * [1,2,3]

### type

리터럴의 자료형을 확인할때 사용한다.

`type(자료형)`

### 숫자형

* 정수
  * 양의 정수, 영, 음의 정수
  * 0o접두어를 통해 8진수
  * 0x를 통해 16진수 가능

* 부동 소숫점형
  * 소수부 생략, 정수부 생략이 가능하다.
  * 매우 큰수, 정밀한수를 위해 지수 표기볍 사용 가능
  * 부동 소숫점 숫자형 리터럴 내의 언더바는 무시됨

* 허수형
  * 파이썬의 허수형은 j접미사가능

### 문자열

문자들의 집합.

큰 따옴표와 작은 따옴표로 표현가능하다.

파이썬은 자료형으로서의 문자형(`char`)은 제공하지 않는다.

`"""` 큰따옴표 3개를 활용해 줄바꿈을 이스케이프 시퀀스가 없이 문자열을 작성할 수 있다.

```py
print("""안녕하세요
줄바꿈을 이스케이프문 없이
할수있다.
""")
```

* 이스케이프 시퀀스
  * 백슬레시 표현 : \\\
  * 큰 따옴표 표현 : \\"
  * 작은 따옴표 표현 : \\'
  * 줄바꿈 표현 : \\n
  * 수평 탭 표현: \\t

## 문자열 포맷팅

문자열 내에 사용된 문자열 표시 유형을 특정 값으로 변경 하는 기법

* %-포맷팅
  * `s` : 문자열 포맷
  * `c` : 문자포맷(정수를 유니코드 문자로 변환해 출력)
  * `d` : 10진 정수 출력
  * `o` : 8진수로 출력
  * `x` : 16진수로 출력
  * `f` : 부동 소수점 숫자로 출력, 소수점 이하 6자리의 정밀도를 기본값으로 가짐
  * `%` : % 문자 자체를 출력

```python
"이름 : %s" % "홍길동"
'이름 : 홍길동'
```

인자로 자료구조 퓨틀과 딕셔너리 자료구조를 사용해서 표현이 가능하다.

```py
"이름 : %(name)s\n나이 : %(age)s세"  % {"name" : "홍길동", "age" : 20}
"이름 : 홍길동\n 나이 :20세"
```

문자열 출력 폭과정렬 방향을 설정할 수 있다.

```py
"%10s" % "우측정렬"
'______우측정렬'
"%-10s" % "좌측정렬"
'좌측정렬______'
```

### str.format()함수를 이용한 문자열 포맷팅

`str.format(args...)`

1. 값의 위치를 이용: 함수에서 전달할 인자의 위치 인덱스는 0부터 시작함
    
    "이름 : {0}, 나이 : {1} 세".format("홍길동", 20)

    "이름 : {1}, 나이 : {0} 세".format("홍길동", 20)
    -> '인자의 순서가 아닌 인덱스 번호가 있는 곳으로 인자가 위치함'

2. 이름 이용 : 함수에서 이름=값 형식으로 인자를 구성하면 이름을 이용해 인자를 전달한다.


    "이름 : {name}, 나이 : {age}세".format(name="홍길동", age=20)

3. 문자열 폭, 정렬방향 지정
   1. 좌측정렬 : "{0:<10}".format("좌측정렬")

    > '좌측정렬______'

   2. 우측정렬 : "{0:>10}".format("우측정렬")

    > '______우측정렬'

   3. 중앙정렬 : "{0:&10}".format("중앙정렬")

    > '\_\_\_중앙정렬___'

## 주석

프로그램의 코드앞에 #을 붕여 작성된부분

