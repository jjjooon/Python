Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("안녕하세요")
안녕하세요
"안녕하세요"
'안녕하세요'
print("100")
100
"100"
'100'
100
100
print("100")
100
print(100)
100
print("%d" % 100)
100
print("%s" % "100")
100
print("%d" % 100) #"%d"(서식) %(구분자) 100(서식의 값)
100
print("100"+"100")
100100
print(100+100)
200
print("%d" % 100+100)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print("%d" % 100+100)
TypeError: can only concatenate str (not "int") to str
print("%d" % (100+100))
200
print("%d" % (100,200))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print("%d" % (100,200))
TypeError: not all arguments converted during string formatting
print("%d %d" % (100))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print("%d %d" % (100))
TypeError: not enough arguments for format string
print("%d %d" % (100, 200))
100 200
print("%d / %d = %d" % (100,200,0.5))
100 / 200 = 0
print("%d / %d = %f" % (100,200,0.5))
100 / 200 = 0.500000
#서식 ==> 숫자(정수(십진수:%d,이진수:%b,팔진수%o 십육진수:%x), 실수:%f) 문자 (한글자:%c, 여러글자:%s)
print("%d" % 123)
123
print("%5d" % 123)
  123
print("%5d" % 123) # 5칸의 공간에 123값이 우로정렬하여 출력
  123
print("%05d" % 123) # 5칸의 공간에 123값이 우로정렬하여 출력하고 빈공간에 0으로 채워라
00123
print("%f" % 123.45)
123.450000
print("%f" % 123.45)#소수점 미만 6자리로 출력
123.450000
print("%7.1f" % 123.45)#전부 7칸 안에 소수점 미만 1자리로 출력(소수점도 한자리)
  123.5
print("%7.3f" % 123.45)#전부 7칸 안에 소수점 미만 3자리로 출력(소수점도 한자리)
123.450
print("%s" % "Python")
Python
print("%10s" % "Python")
    Python
print("%d %5d %05d" % (123, 123, 123))
123   123 00123
print("{0:d} {1:0d} {2:05d}" .format (123, 123, 123))
123 123 00123
print("%d %5d %05d" % (123, 123, 123))#서식을 이용한 출력
123   123 00123
print("{0:d} {1:0d} {2:05d}" .format (123, 123, 123))#포맷함수를 이용한 출력
123 123 00123
#format() : 4호 출력에 사용되는 함수
# \\\\(원표시) 0oOㅇ 1iIlLㅣ
print("\n줄바꿈\n연습")

줄바꿈
연습
print("\t탭\t연습")
	탭	연습
print("글자가 "강조"되는 효과")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("글자가 \"강조\"되는 효과")
글자가 "강조"되는 효과
print("글자가 \'강조\'되는 효과")
글자가 '강조'되는 효과
print("\역슬러시 한 개 출력")
\역슬러시 한 개 출력
print("\\역슬러시 한 개 출력")
\역슬러시 한 개 출력
print("\\역슬러시 두 개 출력")
\역슬러시 두 개 출력
print("\\\\역슬러시 두 개 출력")
\\역슬러시 두 개 출력
print("\\\\\\역슬러시 세 개 출력")
\\\역슬러시 세 개 출력
print("\n\t\'\\그대로 출력")

	'\그대로 출력
print(r"\n\t\'\\그대로 출력")
\n\t\'\\그대로 출력
#탈출문자(이스케이프문자)