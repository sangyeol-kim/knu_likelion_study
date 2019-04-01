# 송현수

# 주석 

### 해당 line이나 function등 설명하기 위한 기능 #으로 시작

```python
>>>  print('Hello World!') # 이곳은 주석이므로 표시되지 않습니다.
Hello World!
```

# 문자열

### 문자나 문자들을 나열한 것 

1. "string"
2. 'string'
3. """string"""
4. '''string'''

```python
>>> my_str1 = "김씨가족"
>>> my_str2 = '김씨가족'
>>> print(my_str1)
김씨가족
>>> type(my_str1)
<class 'str'>

>>> print(my_str2)
김씨가족
>>> type(my_str2)
<class 'str'>

>>> my_str3 = """김씨 #'''도 같은 동작
가족
입니다
"""
>>> my_str3
'김씨\n가족\n입니다\n'
```

### %연산자

1. %d
2. %f
3. %s

```python
>>> my_str = 'My name is %s' % 'Young Choi'
>>> my_str
'My name is Young Choi'

>>> ' %d %d' % (1, 2) # 정수형 숫자를 대입할 때 %d, 여러 숫자 대입 시 () 이용
'1 2'

>>> '%f' % 3.14 # 실수 대입
'3.140000'
```
좀 더 자유롭게 표현하고 대입하기 위해 사용. ( C 스타일을 python에서 차용한 것 )

### '{}'.format()

> %연산자와 결국 기능은 동일하나 좀 더 python스럽게 만들어 놓은 기능

```python
>>> 'My name is {}'.format('송현수')
'My name is 송현수'

>>> '{} x {} = {}'.format(2, 3, 2*3)
'2 x 3 = 6'

>>> '{1} x {0} = {2}'.format(2, 3, 2*3) # 순서 지정시 순서가 바뀔 수 있음.
'3 x 2 = 6'
```

# indexing 1

0 1 **2** 3 4 5 -> index <br/>
P y **t** h o n -> [2]   

- index : 문자의 위치를 뜻함
> 공백도 index에 포함

```python
>>> my_name = "송현수를 사랑해요"

>>> my_name[3]
'를'
>>> my_name[6]
'랑'
```

-6 -5 **-4** -3 -2 -1 -> index <br/>
&nbsp; P&nbsp;&nbsp;y&nbsp;&nbsp; **t**&nbsp;&nbsp; h&nbsp;&nbsp;o &nbsp;&nbsp;n &nbsp;&nbsp; [-4]

# slicing

여러 문자들을 한 번에 나타내기 위해 사용

```python
>>> my_name = "python"
>>> my_name[1:3]
'yt'
>>> my_name[:3]
'pyt'
>>> my_name[2:]
'thon'
```

### string.split()

단위로 나누는 메소드

> () -> 공백 단위
> (':') -> : 단위
> ('n') -> n 단위

```python
>>> my_name = '송현수의 마크다운'
>>> my_name.split()
['송현수의', '마크다운']

>>> fruit_str = '거봉 수박 포도 복숭아'
>>> fruit_str.split()
['거봉', '수박', '포도', '복숭아']
```

### """ 주석

함수 설명을 위해 자주 쓰이는 주석 
> """이것은 주석입니다"""

### print('', end='')

```python
>>> print('집단지성') # default : \n
집단지성
>>> print('집단지성', end='') # 뒤에 공백이 추가됨
집단지성 
>>> print('집단지성', end'/')
집단지성/
```

### \n, \t

* \n : 한 줄 아래로 내려감
* \t : 기본 띄어쓰기보다 넓은 tab

# List

> mutable : 값을 변경할 수 있음 <br/>
> 문자열은 값을 변경할 수 없음


```python
>>> my_list = []
>>> my_list
[]
>>> type(my_list)
<class 'list>

>>> my_list = [1, 2, 3]
>>> my_list
[1, 2, 3]

>>> my_list.append(4) # 리스트에 추가하는 메소드
>>> my_list
[1, 2, 3, 4]
```

# indexing 2

> 리스트에서의 인덱싱도 같은 맥락속에서 동작한다.<br/>
> indexing과 마찬가지로 slicing도 같음.

```
>>> animals = ['사자', '코알라', '개', '고양이']
>>> animals[1]
'코알라'

>>> del animals[1]
>>> animals
['사자', '개', '고양이']
```

### list.sort()

- list를 정렬해주는 메소드
- 숫자면 오름차순, 한글이면 ㄱㄴㄷㄹ... 영어면 abcd...

### list.count()

- list.count('n') : 리스트 내 n의 갯수

### len(list)

- list내의 요소의 갯수

# Tuple

> list와 비슷. <br/>
> immutable : 값을 변경할 수 없음


```python
>>> my_tuple = ()
>>> my_tuple
()

>>>type(my_tuple)
<class 'tuple>

>>> my_tuple = 1,2,3
>>> my_tuple
(1, 2, 3)
```

# Packing, Unpacking

> Packing의 예
```python
>>> my_tuple = 1, 2, 3
```

> Unpacking의 예
```python
>>> num1, num2, num3 = my_tuple
>>> num1 
1
>>> num2
2
>>> num3
3
```

> 응용

```python
>>> num1, num2 = num2, num1
>>> num1
2
>>> num2
1
```




