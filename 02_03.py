Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=123
type(a)
<class 'int'>
#변수에 값을 넣는 순간에 변수의 데이터형이 결정된다
a=100**100
print(a)
100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#int의 크기에는 제한이 없다.
a=0xFF
b=0o77
c=0b1111
print(a,b,c)
255 63 15
#정수형에는 16진수, 8진수, 2진수도 사용할 수 있다.
a=3.14
b=3.14e5
print(a,b)
3.14 314000.0
b=3.14e5 #3.14* 10의 5승을 의미한다.
a=10; b=20
print(a+b,a-b,a*b,a/b)
30 -10 200 0.5
#정수 및 실수 데이터형은 사칙 연산 +, -, *, /를 수행할 수 있다.
a,b=9,2
print(a**b, a%b,a//b)
81 1 4
#제곱을 의미하는 **, 나머지를 구하는 %, 나눈 후에 소수점을 버리는 // 연산자도 사용할 수 있다.
a=True
type(a)
<class 'bool'>
#불(Bool)형은 참(True)이나 거짓(False)만 저장할 수 있다.
a=(100==100)
b=(10>100)
print(a,b)
True False
#불형은 비교의 결과를 참이나 거짓으로 저장하는 데 사용될 수도 있다.
a="파이썬 만세"
a
'파이썬 만세'
print(a)
파이썬 만세
type(a)
<class 'str'>
#문자열을 ‘abc’, “파이썬 만세”, “1” 등 문자집합을 의미한다. 
#문자열은 양쪽을 큰따옴표(“)나 작은따옴표(‘)로 감싸야 한다.
"작은따옴표는 '모양이다."
"작은따옴표는 '모양이다."
'큰따옴표는 "모양이다.'
'큰따옴표는 "모양이다.'
#문자열 중간에 작은따옴표나 큰따옴표를 출력하고 싶다면 다른 따옴표로 묶어 주면 된다.
a="이건 큰타옴표 \"모양"
a
'이건 큰타옴표 "모양'
#역슬래시(\) 뒤에 큰따옴표나 작은따옴표를 사용해도  글자로 인식한다.
a = "파이썬\n만세'
SyntaxError: unterminated string literal (detected at line 1)
a = '파이썬\n만세'
print(a)
파이썬
만세
a="""파이썬
만세"""
a
'파이썬\n만세'
print(a)
파이썬
만세
#문자열을 여러 줄로 넣으려면 중간에 \n을 포함시키면 된다.
#작은따옴표나 큰따옴표 3개를 연속해서 묶어도 된다.