Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=5; b=3
print(a+b,a-b,a*b,a/b,a//b,a%b,a**b)
8 2 15 1.6666666666666667 1 2 125
#a//b는 a를 b로 나눈 몫이고, a%b는 a를 b로 나눈 나머지값
#산술 연산자의 종류(=(대입연산자),+,-,*,/,//,%.**)
#세미콜론(;)은 앞뒤를 완전히 분리. 그러므로 a=5; b=3은 다음과 동일하다. 
#또 콤마(,)로 분리해서 값을 대입할 수도 있어 a, b=5, 3 도 동일
s1,s3,s3="100","100.123","99999"
print(int(s1)+1,float(s2)+1,int(s3)+1)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(int(s1)+1,float(s2)+1,int(s3)+1)
NameError: name 's2' is not defined. Did you mean: 's1'?
s1,s2,s3="100","100.123","99999"
print(int(s1)+1,float(s2)+1,int(s3)+1)
101 101.123 100000
#산술 연산을 하는 문자열과 숫자의 상호 변환
#문자열이 숫자로 구성되어 있을 때, int() 또는 float() 함수 사용해서 정수나 실수로 변환
#문자열을 int() 함수가 정수로, float() 함수가 실수로 변경
# float():9호 ==> 실수로 변환하는 함수
a = 100; b=100.123
str(a)+'1';str(b)+'1'
'1001'
'100.1231'
#숫자를 문자열로 변환하려면 str() 함수 사용. 
#a와 b가 문자열로 변경되어 100+1이 아닌 문자열의 연결인 ‘1001’과 ‘100.1231’ 됨
#print() 함수는 출력 결과에 작은따옴표가 없어 문자열인지 구분하기가 어려워 사용하지  않음
a=10
a+=5;print(a) #a+=5가 a=a+5이다
15
a-=5;print(a) #a-=5가 a=a-5이다
10
a*=5;print(a) #a*=5가 a=a*5이다
50
a/=5;print(a) #a/=5가 a=a/5이다
10.0
a//=5;print(a) #a//=5가 a=a//5이다
2.0
a%=5;print(a) #a%=5가 a=a%5이다
2.0
a**=5;print(a) #a**=5가 a=a**5이다
32.0
#산술 연산자와 대입 연산자 
#대입 연산자 = 외에도 +=, -=, *=, /=, %=, //=, **= 사용
#예) 첫 번째 대입 연산자 a+=3은 a에 3을 더해서 다시 a에 넣으라는 의미로 a=a+3과 같음
#Tip • 파이썬에는 C/C++, 자바 등의 언어에 있는 증가 연산자 ++나 감소 연산자 --가 없음
