#제어문
# 조건문

a=15
if( a<20 ):
    print('미성년')
    print('집에가')
else:
    print('환영합니다')
    print('문라이트입니다')
print('조건문과 상관없음')


score= 75
if( 90 <= score <=100):
    print("A 학점")
elif( score>= 80):
    print('B 학점')
elif( score>= 70 ):
    print('C 학점')
elif( score >= 60):
    pass

#switch와 같은 분기문은 없음
a=0
while(a<5):
    print('a:',a)
    a= a+1


n=0
while(True):
    print(n)
    n += 1
    if(n==10):
        break

for i in range(10):
    print('i:',i)

for i in range(5,10):
    print('i:',i)

for n in range(1,11):
    if(n==5):
        break
    print("n:",n)

for n in range(1,11):
    if(n==5):
        continue
    print("n:",n)
