money, c500, c100, c50, c10 = 0, 0, 0, 0, 0
#동전으로 교환할 돈(money)과 500원, 100원, 50원, 10원짜리 동전의 개수를 저장 할 변수 초기화

money = int(input("교환할 돈은 얼마?"))

c500 = money // 500#500원짜리 동전의 개수를 구함
money %= 500#다시 money를 500으로 나눈 후 나머지 값 저장 money%=500은 money=money%500과 동일. 

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print("500원짜리 ==> %d개" % c500)
print("100원짜리 ==> %d개" % c100)
print("50원짜리 ==> %d개" % c50)
print("10원짜리 ==> %d개" % c10)
print("바꾸지 못한 잔돈 ==> %d원" % money)#마지막 money에 저장된 값은 10 미만으로, 바꿀 수 없는 나머지 돈

