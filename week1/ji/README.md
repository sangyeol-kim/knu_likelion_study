# 파이썬 정리

> [미운코딩오리새끼](https://www.youtube.com/playlist?list=PLGPF8gvWLYyrkF85itdBHaOLSVbtdzBww) 유투브 강좌를 이용해 파이썬의 기본적인 문법을 정리한 노트입니다.
> 작성자 : 지현규
> 정리구간 : #27 ~ #40
> [파이썬튜터](http://pythontutor.com/) 를 사용하여 변수가 어떻게 저장되는지 확인가능

## 파이썬의 연산자

여러종류의 연산을 위해 다양한 연산자(Operator)를 제공한다.
자료형에 따라 갖는 의미가 달라지기도 한다.

### 1. 산술연산자

- 두 개의 피연산자를 연산하는 기능

* 사칙연산

```python
>>> a=5
>>> b=3
```

```python
a+b   //더하기
>>> 8

a-b   //빼기
>>> 2

a*b   //곱하기
>>> 15

a/b   //나누기
>>> 1.6666666666666667
```

- 나누기(몫)

```python
a//b
>>> 1
```

- 나머지

```python
a%b
>>> 2
```

- 제곱

```python
a**b
>>> 125
```

> String(문자열)에서의 + 와 \*

```python
"안녕" + "하세요"
>>> 안녕하세요
"안녕하세요" * 3
>>> 안녕하세요안녕하세요안녕하세요
```

> [] 리스트에서의 + 와 \*

```python
[1,2,3,4,5] + [6,7,8,9,10]
>>> [1,2,3,4,5,6,7,8,9,10]
[1,2,3] * 3
>>> [1,2,3,1,2,3,1,2,3]
```

### 2. 대입연산자(할당연산자)

- 우항의 데이터를 좌항의 변수에 대입(할당)

```python
a = 4
b = 3.141592
str = 'Hello'
```

- 복합대입연산자

```python
a = 2
a = a + 1
>>> a = 3
```

> 위의 수식처럼 대입연산자를 기준으로 같은 변수가 위치하고 있다면 좀더 "복합대입연산자" 를 사용하여 좀더 간단하게 나타낼 수 있다.

```python
a += 2    // a = a + 2
a -= 2    // a = a - 2
a *= 2    // a = a * 2
a /= 2    // a = a / 2
a //= 2   // a = a // 2
a %= 2    // a = a % 2
a **= 2   // a = a ** 2
```

> 하지만 파이썬에는 C/ 자바등의 언어에 있는 증가연산자 ++나 감소 연산자 --가 없다.

```phyton
a++
a--
>>> 오류
```

### 3. 관계연산자

- 어떤것이 크거나 작거나 같은지 비교하는 것
  (참 = True / 거짓 = False 로 표시)

```python
a, b = 1, 3

a == b  // 두 값이 같으면 참
>>> False

a != b  // 두 값이 다르면 참
>>> True

a > b
>>> False

a < b
>>> True

a >= b  // 크거나 같다.
>>> False

a >= b  // 작거나 같다.
>>> True
```

### 4. 논리연산자

- and(그리고), or(또는), not(부정) 세 가지 종류
  예) a라는 값이 100과 200 사이에 들어 있어야 한다는 조건 표현

```python
(a > 100) and (a < 200)
```

```python
(a > 100) and (a< 200)
>>> a가 100보다 크다 그리고 200보다 작다
>>> 둘 다 참이면 True

(a > 100) or (a< 200)
>>> a가 100보다 크다 또는 200보다 작다
>>> 둘 중 하나만 참이면 True

not(a < 100)
>>> a가 100보다 작지 않다
>>> 참이면 False, 거짓이면 True
```

### 5. 비트연산자

- 정수를 2진수로 변환한 후 각 자리의 비트끼리 연산 수행
- 비트 연산자의 종류 : &, |, ^, ~, <<, >>

```python
10 & 7
123 & 456
0xFFFF & 0x0000
>>> 2 72 0
```

> 123 & 456은
> 123의 2진수 : 1111011
> 456의 2진수 : 111001000
> 123 & 456 : 1001000
> 논리곱의 "True = 1 / False = 0" 과 같다

### 6. 맴버쉽연산자

- 컨테이너에 들어있는지 확인하는 연산자
- in 과 not in
- 찾을데이터 [not]in 컨테이너

```python
numList = [1,2,3,4,5]
1 in numList
>>> True

7 in numList
>>> False

strList = ['grape', 'strawberry' 'melon']
'melon' in  strList
>>> True

'apple' not in strList
>>> True
```

> for문에서 사용되는 in은 다르게 사용

```phyhon
numList = [1,2,3,4,5]
for num in numList :
// 컨테이너(numList)에서 원소 하나씩 num으로 가져온다.

```

## range()

- start부터 end까지 1씩 증가하는
- range(start, end+1)
- range() 내장함수

```python
# range는 내장함수다
>>> range(3)
range(0,3) # == [0,1,2]
>>> range(3,5)
range(3,5) # == [3,4]
>>> type(range(3))
<class 'range'>

# for문과 함께 자주사용됨
for n in range(0,100) :
  print(n)
>>> 0
>>> 1
>>> ...
>>> 99
```

## 제어문법

### 조건문

#### if - elif - else

```python
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
elif 조건문 :
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B
    ...
```

조건문을 테스트해서 참이면 if문 바로 다음의 문장(if 블록)들을 수행하고, 조건문이 거짓이면 else문 다음의 문장(else 블록)들을 수행하게 된다. 그러므로 else문은 if문 없이 독립적으로 사용할 수 없다.

"C나 JAVA의 switch문 또한 없다"

### 반복문

반복해서 문장을 수행해야 할 경우 while문을 사용한다. 그래서 while문을 반복문이라고도 부른다.

#### while

```python
while 조건문 :
    수행할 문장1
    수행할 문장2
    수행할 문장3
    ...
```

while문은 조건문이 참인 동안에 while문 아래에 속하는 문장들이 반복해서 수행된다.
그러므로 break와 continue의 적절한 사용이 필요하다.

#### for

```python
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
```

리스트나 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례로 변수에 대입되어 "수행할 문장1", "수행할 문장2" 등이 수행된다.

만약 변수를 따로 사용하고 싶지않고 반복만 하고 싶다면
변수대신 \_를 사용하여 메모리를 절약할 수 있다.

## 문자열 format

### 문자열.format()

- 문자열의 대괄호 자리에 format 뒤의 괄호안에 들어있는 값을 하나씩 넣는다
- 문자열에 포함된 대괄호 개수보다 format안에 들어있는 값의 수가 많으면 정상동작

```python
print('{} 번 손님'.format(number, greeting))
```

- 문자열에 포함된 대괄호 개수 보다 format안에 들어잇는 값의 수가 적으면 에러

```python
print('{} 번 손님 {}'.format(number))
```

- 문자열을 출력하는 여러가지 방법

```python
number = 20
welcome = '환영합니다'
base = '{} 번 손님 {}'

# 모두 같은 print
print(number, '번 손님', welcome)
print(base.format(number, welcome))
print('{} 번 손님 {}'.format(number,welcome))
print('%d 번 손님 %s' %(number, welcome))
>>> 20번 손님 환영합니다
```

- format의 출력순서 바꾸기

```python
number = 10
day = "three"
# 인덱스주기
"{1} {0}".format("환영합니다", "손님")
>>> 손님 환영합니다

# 변수명주기
"{w} {s}".format(s="손님",w="환영")
>>> 환영 손님
```

## 이중 for문과 .format

```python
 for j in range(2,10) :
   for i in range(1,10) :
     print('{}x{}={}'.format(j,i,j*i))

>>> 2x1=2
>>> 2x2=4
>>> 2x3=6
...
>>> 9x9=81
```

## 컴프리핸션

#### 리스트 = [수식 for 항목 in range() if 조건식]

- 값이 순차적인 리스트를 한 줄로 만드는 간단한 방법

```python
# 1부터 5까지 저장된 리스트를 만드는 방법
numlist = []
for num in range(1,6) :
  numlist.appned(num)
numList
>>> [1,2,3,4,5]

# 위 코드를 컴프리핸션으로 한줄로 가능
numlist = [num for num in range(1,6)]
numlist
>>> [1,2,3,4,5]

# 조건을 붙이는 것도 가능
oddlist = [num for num in range(1,11) if num % 2 == 1]
oddlist
>>> [1,3,5,7,9]

# 수식도 가능
powlist = [num*num for num in range(1,6)]
powlist
>>> [1,4,9,16,25]
```

## 함수

#### [Python Documents](https://docs.python.org/ko/3/)

인자를 주고, 처리하여 반환값(return)을 받음

#### Why ? Function

- 다시 사용할 수 있다
- 코드를 관리하기 쉽다
- 조립해서 사용할 수 있다

### 내장함수

- 파이썬에서 기본적으로 제공하는 함수
- 이름만 알면 사용가능

### 모듈의 함수

- 이미 만들어논 함수뭉치
- 모듈을 먼저 import하여 사용
- 모듈.함수명(인자)
- ex) Random모듈

```python

// import로 모듈추가
import random

// random모듈의 choice사용 : 리스트에서 무작위로 하나를 return
students = ['사과', '망고', '고등어', '갈치', '오이', '호박', '감자']
print(random.choice(students))
>>> 호박
```

### 사용자 정의함수

- 직접 만든 함수

```python
def 함수이름(인자1, ...) :
   실행할 명령:
   실행할 명령:
   return 결과
```

- return값이 하나인 함수

```python
def add(num1, num2) :
  return num1+num2

add(1,2)
>>> 3
```

- return 값이 2개 이상인 함수

```python
def add_mul(num1, num2) :
  return num1+num2, num1*num2

add(1,2)
>>> (3,2)

val1, val2 = add_mul(1,2)
print(val1, val2)
>>> 3 2
```

> 두개의 값을 return 해주는 것이 아니라
> 두개의 값을 Packing을 통해 튜플로 반환
> 즉 함수는 한개의 튜플() 을 반환한다

## Unpacking과 Packing

우항의 값이 여러개일 경우 Packing
좌항의 개수와 우항 컨테이너의 원소개수가 동일하다면 Unpacking
결국 List[] Turple() Dictionary{:} set{}
모두 Unpacking 과 Packing이 가능하고
각각의 원소의 개수에 맞게 좌항 존재필수

```python
// 우항의 튜플()로 Packing
num1 = 1,2
print(num1)
>>> (1,2)

// 다량의 변수 초기화시 응용
// 리스트[]의 *연산을 사용하여 0으로 초기화
num1, num2, num3, num4, num5 = [0]*5
num1, num2, num3, num4, num5 = [1,2,3,4,5]
// 오류 > 왜? 리스트()가 아닌 단항연산자()로 인식
num1, num2, num3, num4, num5 = (0)*5

// List[] Turple() 모두 Unpacking 가능

num1, num2 = 1,2
print(num1, num2)
>>> 1, 2

num1, num2 = [1,2]
print(num1, num2)
>>> 1, 2

num1, num2 = (1,2)
print(num1, num2)
>>> 1, 2

//Packing과 Unpaking을 사용하여 두개의 변수값을 쉽게 교환가능

num1, num2 = num2, num1
print(num1, num2)
>>> 2 1


// Dictionary{:}의 경우 key값으로 Unpaking

dic = {"한":"국", "만":"세"}

num1, num2 = dic
print(num1, num2)
>>> '한' '만'

dic.keys()
>>> dict_keys(['한', '만'])

num1, num2 = dic.keys()
print(num1, num2)
>>> '한' '만'

//Dictionary{:} Value값 Unpacking

dic.values()
>>> dict_values(['국', '세'])
num1, num2 = dic.values()
print(num1, num2)
>>> '국' '세'

//Dictionary{:} Value에 중복값('국') 추가

dic['민'] = '국'
dic
>>> {"한":"국", "만":"세", "민":'국"}
dic.values()

//set{}도 Unpacking 가능

>>> dict_values(["국", "세", "국"])
setEx = set(dic.values())
>>> {"국", "세"}

num1, num2 = setEx
print(num1, num2)
>>> '국' '세'

//< dic.items() >는 (키:벨류)튜플의 원소를 가진 리스트[] 반환

dic.items()
>>>dict_items([('한', '국'), ('만', '세'), ('민', '국')])

// 리스트[] 각 원소인 튜플()로 Unpacking

num1, num2, num3 = dic.items()
print(num1, num2, num3)
>>>('한', '국') ('만', '세') ('민', '국')

// key와 value값을 한번에 Unpacking하고 싶다면 for문 사용

for num1, num2 in dic.items() :
  print(num1, num2)
>>> 한 국
>>> 만 세
>>> 민 국


// 리스트[]안에 하나의 튜플()이 있다면 Unpacking 오류

num1, num2 = [(1, 2)]
>>> ValueError : not enough values to Unpacking


// 튜플() 안에 하나의 리스트[]나 튜플()이 있다면 Unpacking

num1, num2 = ([1, 2])
print(num1, num2)
>>> 1, 2

num1, num2 = ((1,2))
print(num1, num2)
>>> 1, 2

//리스트[]와 튜플()모두 두개이상의 원소를 가지고 있다면 Unapcking

num1, num2 = [(1,2),(4,5)]
print(num1, num2)
>>> (1, 2) (4, 5)

num1, num2 =([1,2], [3,4])
>>>print(num1, num2)
[1, 2] [3, 4]
```

## 객체

- 객체 = 데이터 + 함수(메소드)
- 사용 : 객체명.메소드(인자)

```python
my_list = [1,2,3]
my_list.appened(4) //my_list 객체의 append 메소드사용
```

## PEP8

- 파이썬 코딩 가이드라인
- [Python PEP 8](https://www.python.org/dev/peps/pep-0008/)
- [번역본](https://yoonpunk.tistory.com/1)
