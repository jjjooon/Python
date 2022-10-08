Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a, b =100, 200
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)
False True False True False True
print(a=b)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(a=b)
TypeError: 'a' is an invalid keyword argument for print()
#a와 b를 비교하는 관계 연산자 ==를 사용하려다 착오로 =을 하나만 쓴 코드
#빨간색 오류로 나타남. a=b는 b 값을 a에 대입하라는 의미이지 관계 연산자가 아님
#관계연산자의 개념
#어떤 것이 크거나 작거나 같은지 비교하는 것(참은 True로, 거짓은 False로 표시)
#주로 조건문(if)이나 반복문(while)에서 사용, 단독으로는 거의 사용하지 않음
#관계연산자의 종류
#==, !=(같지 않다), >,<,>=,<=
a=99
(a>100) and(a<200)
False
(a>100) or(a<200)
True
not(a==100)
True
#논리 연산자의 종류와 사용
#and(그리고), or(또는), not(부정) 세 가지 종류
#예) a라는 값이 100과 200 사이에 들어 있어야 한다는 조건 표현
(a>100)and(a<200) #예) a라는 값이 100과 200 사이에 들어 있어야 한다는 조건 표현
False
if(1234):print("참이면 보여요")

참이면 보여요
if(0):print("거짓이면 안보여요")

