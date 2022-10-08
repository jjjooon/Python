Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=100
b=50
result=a+b
a
100
b
50
result
150
print(a,+,b,=,result)
SyntaxError: invalid syntax
print(a,'+',b,'=',result)
100 + 50 = 150
print(a,'-',b,'=',result)
100 - 50 = 150
result=a-b
print(a,'-',b,'=',result)
100 - 50 = 50
result=a*b
print(a,'*',b,'=',result)
100 * 50 = 5000
result=a/b
print(a,'/',b,'=',result)
100 / 50 = 2.0

========================== RESTART: D:/Psung/01_03.py ==========================
100 + 50 = 150

========================== RESTART: D:/Psung/01_03.py ==========================
100 + 50 = 150
100 - 50 = 50
100 * 50 = 5000
100 / 50 = 2.0

========================== RESTART: D:/Psung/01_03.py ==========================
100 + 50 = 150
100 - 50 = 50
100 * 50 = 5000
100 / 50 = 2.0

========================== RESTART: D:/Psung/01_03.py ==========================
100
50
100 + 50 = 10050
Traceback (most recent call last):
  File "D:/Psung/01_03.py", line 28, in <module>
    result=a-b
TypeError: unsupported operand type(s) for -: 'str' and 'str'
'100'+'50'
'10050'
'100'-'50'
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    '100'-'50'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
100+50
150
100-50
50
# 100(숫자) + 50(숫자)일때 '+'는 산술연산자
# '100'(숫자) + '50'(숫자)일때 '+'는 연결연산자
#  '연결연산자는 '+'에만 적용 '-'는 에러
# '100'(문자) + '50'(문자)일때 '+'는 연결연산자
#  '연결연산자는 '+'에만 적용 '-'는 에러