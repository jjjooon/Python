'''
a=100
b=50
result=a+b
print(a,'+',b,'=',result)
result=a-b
print(a,'-',b,'=',result)
result=a*b
print(a,'*',b,'=',result)
result=a/b
print(a,'/',b,'=',result)
'''
'''
콘솔창
 - 한줄에 한문장이 기본
 - 이미 끝난 문장은 수정이 안됨
 - 같은창에서 결과를 즉시볼수 있음

스크립트창
 - 한줄에 여러문장이 가능
 - 이미 끝난 문장도 수정이 됨
 - 스트립트 창에서 작성한 결과를 콘솔창에서 볼수 있음
'''
'''
a=input()
b=input()
result=a+b
print(a,'+',b,'=',result)
result=a-b
print(a,'-',b,'=',result)
result=a*b
print(a,'*',b,'=',result)
result=a/b
print(a,'/',b,'=',result)
'''
'''
print() 출력함수(1호)
input() 입력함수(2호) ==> 문자형 문자(가,A), 숫자형 문자(100(일영영), 50(오영)) input()입력되는 모든데이터는 문자임
int() 정수형함수(3호) ==>숫자형문자를 정수(문자)로 변환해주는 함수
int(input()) = "숫자를 입력하세요" 할때사용(한단어로 외우세요)
'''
'''
a=int(input("첫 번째 숫자를 입력하세요 : "))
b=int(input("두 번째 숫자를 입력하세요 : "))
result=a+b
print(a,'+',b,'=',result)
result=a-b
print(a,'-',b,'=',result)
result=a*b
print(a,'*',b,'=',result)
result=a/b
print(a,'/',b,'=',result)
'''
a=int(input("첫 번째 숫자를 입력하세요 : "))
b=int(input("두 번째 숫자를 입력하세요 : "))
c=int(input("세 번째 숫자를 입력하세요 : "))
d=int(input("네 번째 숫자를 입력하세요 : "))
result=a+b+c+d
print(a,'+',b, '+',c,'+',d,'=',result)
result=a-b-c-d
print(a,'-',b,'-',c,'-',d,'=',result)
result=a*b*c*d
print(a,'*',b,'*',c,'*',d,'=',result)
result=a/b/c/d
print(a,'/',b,'/',c,'/',d,'=',result)
