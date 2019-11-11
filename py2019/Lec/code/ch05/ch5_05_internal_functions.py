# ch5_05_internal_functions.py
#
print("내장 함수")
#######################################
#
# 파이썬 내장 함수는 미리 준비된 내부 모듈
# 외부 모듈과 달리 import가 필요하지 않다.
#
#######################################
#

print("abs()")
#######################################
# abs(x)는 어떤 숫자를 입력받았을 때,
# 그 숫자의 절댓값을 돌려주는 함수
#######################################
#
abs(3)
abs(-3)
abs(-1.2)

print("all()")
###########################################################
# all(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며
# 이 x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다.
###########################################################
#
all([1, 2, 3])
all([0, 1, 2, 3])

# 참고
bool([0, 1, 2, 3]), bool([0]), bool((0)), bool((0,))

print("any()")
###########################################################
# any(x)는 x 중 하나라도 참이 있으면 True를 돌려주고,
# x가 모두 거짓일 때에만 False를 돌려준다. all(x)의 반대이다.
###########################################################
#
any([0, 1, 2, 3])

any([0, ""])


print("chr()")
###########################################################
# chr(i)는 아스키(ASCII) 코드 값을 입력받아
# 그 코드에 해당하는 문자를 출력하는 함수이다.
###########################################################
#
chr(97)
chr(48)


print("dir()")
###########################################################
# dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다.
###########################################################
#
dir([1, 2, 3])  # list object

dir({"1": "a"})  # dict object
type({"1": "a"})


print("divmod()")
###########################################################
# divmod(a, b)는 2개의 숫자를 입력으로 받는다.
# 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수
###########################################################
#
divmod(7, 3)  # 결과값을 tuple로 반환


print("enumerate()")
###########################################################
# enumerate는 "열거하다"라는 뜻이다.
# 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로
# 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
###########################################################
#
for i, name in enumerate(["body", "foo", "bar"]):
    print(i, name)


print("eval()")
###########################################################
# eval(expression )은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을
# 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수
###########################################################
#
eval("1+2")
eval("'hi' + 'a'")
eval("divmod(4, 3)")


print("filter()")  # ***
###########################################################
# filter 함수는 첫 번째 인수로 함수 이름을,
# 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다.
# 그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인
# 함수에 입력되었을 때 반환 값이 참인 것만 묶어서(걸러 내서) 돌려준다.
###########################################################
#
# positive.py
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result


print(positive([1, -3, 2, 0, -5, 6]))

# filter() 함수 이용
# filter1.py
def positive(x):
    return x > 0


list(filter(positive, [1, -3, 2, 0, -5, 6]))

# lambda를 사용하면 더욱 간편하게 코드를 작성할 수 있다.

list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
###########################################################


print("hex()")
###########################################################
# hex(x)는 정수 값을 입력받아 16진수(hexadecimal)로
# 변환하여 돌려주는 함수
###########################################################
#
hex(10)
hex(234)


print("id()")
###########################################################
# d(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수
###########################################################
#
a = 3
id(3)
id(a)
b = a
id(b)
id(4)  # different address


print("input()")
###########################################################
# input([prompt])은 사용자 입력을 받는 함수이다.
# 매개변수로 문자열을 주면, 그 문자열은 프롬프트가 된다.
###########################################################
#
a = input()
b = input("Enter: ")
b


print("int()")
###########################################################
# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을
# 정수 형태로 돌려주는 함수
###########################################################
#
int(3)
int("3")
int(3.14)

# int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환
int("11", 2)
int(11, 2)  # TypeError:

int("F", 16)


print("isinstance()")
###########################################################
# isinstance(object, class )는 첫 번째 인수로 인스턴스,
# 두 번째 인수로 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여
# 참이면 True, 거짓이면 False를 돌려준다.
###########################################################
#
class Person:
    pass


a = Person()
isinstance(a, Person)

b = 3
isinstance(b, Person)


print("len()")
###########################################################
# len(s)은 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수이다.
###########################################################
#
len("python")
len([1, 2, 3])
len((1, "a"))
len({a: 3})


print("list()")
###########################################################
# list(s)는 반복 가능한 자료형 s를 입력받아
# 리스트로 만들어 돌려주는 함수
###########################################################
#
list("python")
list((1, 2, 3))


print("map()")  # ***
###########################################################
# map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을
# 입력으로 받는다.
# map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를
# 묶어서 돌려주는 함수
###########################################################
#
# two_times.py
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result


result = two_times([1, 2, 3, 4])
print(result)

# map 함수를 사용
def two_times(x):
    return x * 2


list(map(two_times, [1, 2, 3, 4]))

# lambda를 사용
list(map(lambda a: a * 2, [1, 2, 3, 4]))
###########################################################


print("max()")
###########################################################
# max(iterable)는 인수로 반복 가능한 자료형을 입력받아
# 그 최댓값을 돌려주는 함수
###########################################################
#
max([1, 2, 3])
max("python")
max(list(range(10)))
max(range(10))


print("min()")
###########################################################
# min(iterable)은 max 함수와 반대로, 인수로 반복 가능한
# 자료형을 입력받아 그 최솟값을 돌려주는 함수
###########################################################
#
min([1, 2, 3])
min("python")
min(range(10))


print("oct()")
###########################################################
# oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수
###########################################################
#
oct(9)
oct(12345)


print("ord()")
###########################################################
# ord(c)는 문자의 아스키 코드 값을 돌려주는 함수
# ※ ord 함수는 chr 함수와 반대이다.
###########################################################
#
ord("a")  # chr(97)
ord("0")


print("pow()")
###########################################################
# pow(x, y)는 x의 y 제곱한 결괏값을 돌려주는 함수
###########################################################
#
pow(2, 4)  # 2**4
pow(3, 4)  # 3**4


print("range()")  # ***
###########################################################
# range([start,] stop [,step] )는 for문과 함께 자주 사용하는 함수
# 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로
# 만들어 돌려준다.
###########################################################
#
# 인수가 하나일 경우
list(range(5))

# 인수가 2개일 경우
list(range(5, 10))

# 인수가 3개일 경우
list(range(1, 10, 2))

list(range(0, -10, -1))


print("round()")
###########################################################
# round(number[, ndigits]) 함수는 숫자를 입력받아 반올림해 주는 함수
# ※ [, ndigits]는 ndigits가 있을 수도 있고 없을 수도 있다는 의미이다.
###########################################################
#
round(4.6)
round(4.2)

# 소수점 2자리까지만 반올림
round(5.678, 2)


print("sorted()")  # ***
###########################################################
# sorted(iterable) 함수는 입력값을 정렬한 후
# 그 결과를 리스트로 돌려주는 함수
# 'reverse' 속성으로 정렬순서 반전
###########################################################
#
sorted([3, 1, 2])
sorted([3, 1, 2], reverse=True)

sorted(["a", "c", "b"])
sorted(["a", "c", "b"], reverse=True)

sorted("zero")
sorted((3, 2, 1))  # list로 반환!!!
###########################################################


print("str()")
###########################################################
# str(object)은 문자열 형태로 객체를 변환하여 돌려주는 함수
###########################################################
#
str(3)
str(100)
str("hello".upper())


print("sum()")
###########################################################
# sum(iterable) 은 입력받은 리스트나 튜플의
# 모든 요소의 합을 돌려주는 함수
###########################################################
#
sum([1, 2, 3])
sum((4, 5, 6))


print("tuple()")
###########################################################
# tuple(iterable)은 반복 가능한 자료형을 입력받아
# 튜플 형태로 바꾸어 돌려주는 함수
###########################################################
#
tuple("abc")
tuple([1, 2, 3])


print("type()")
###########################################################
# type(object)은 입력값의 자료형이 무엇인지 알려 주는 함수
###########################################################
#
type("abc")
type([])
type({a: 4})
type(open("test", "w"))


print("zip()")  # ***
###########################################################
# zip(*iterable)은 동일한 개수로 이루어진 자료형을
# 묶어 주는 역할을 하는 함수
###########################################################
#
list(zip([1, 2, 3], [4, 5, 6]))
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
list(zip("abc", "def"))
list(zip([1, 2, 3], "def"))

############## The END  ##############


"""
Author: redwoods
파이썬 코드: ch5_05_internal_functions.py
"""
