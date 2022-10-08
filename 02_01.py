Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
boolVar = True
intVar = 0
floatVar = 0.0
strVar = ""
boolVar, intVar, floatVar, strVar = True, 0, 0.0, ""
boolVar, intVar, floatVar, strVar = False, 100, 123.45, "안녕?"
type(boolVar),type(intVar),type(floatVar),type(strVar)
(<class 'bool'>, <class 'int'>, <class 'float'>, <class 'str'>)
#type():5호 데이형을 알고자 할때
#변수의 선언
#변수는 어떠한 값을 저장하는 메모리 공간(그릇)
#변수 선언은 그릇을 준비하는 것
#파이썬은 C/C++, 자바 등과는 달리 변수를 선언하지 않아도 되지만 긴 코드를 작성할 때는 사용될 변수를 미리 계획적으로 준비하는 것이 더 효율적
#가장 많이 사용하는 변수는 불형(Boolean, True 또는 False 저장), 정수형, 실수형, 문자열
#변수명 규칙
#대·소문자를 구분한다( myVar와 MyVar는 다른 변수).
#문자, 숫자, 언더바(_)를 포함할 수 있다. 하지만 숫자로 시작하면 안 된다( var2(O), _var(O), var_2(O), 2Var(X)).
#예약어는 변수명으로 쓰면 안 된다. 파이썬의 예약어는 True, False, None, and, or, not, break, continue, return, if, else, elif, for, while, except, finally, gloval, import, try 등이다.
#변수의 사용(1)
#변수는 값을 담으면(대입하면) 사용 가능. 변수에 있던 기존 값은 없어지고 새로 입력한 값으로 변경됨
#변수에는 변수의 값을 넣을 수도 있고, 계산 결과를 넣을 수도 있음
var2 =200
var1 =var2
var1
200
var1=100+100
var1
200
var1=var2+100
var1
300
#변수에는 숫자와 변수의 연산을 넣을 수도 있음
var1=var2=var3=var4=100
var1
100
#변수에 연속된 값을 대입하는 방식
var1=var1+200
var1
300
#변수에 연산 결과를 자신의 값으로 다시 대입하는 방식
myVar=100
type(myVar)
<class 'int'>
myVar=100.0
type(myVar)
<class 'float'>
#파이썬에서 변수의 데이터 형식은 값을 넣는 순간마다 변경될 수 있는 유연한 구조
10=100
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
#대입 연산자의 왼쪽에는 무조건 변수만 올 수 있고, 오른쪽에는 무엇이든(값, 변수, 수식, 함수 등) 올 수 있음