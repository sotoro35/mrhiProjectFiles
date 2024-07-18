# 연산자
a= 10
b= 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a%b) #나머지
print(a//b) #몫

x,y = divmod(a,b) # 몫과 나머지
print(x)
print(y)

print( b**2 ) #제곱
print( b**3 ) #3제곱
print( b**(1/2) ) #제곱근

print( a>b )
print( a<b )
print( a>=b )
print( a<=b )
print( a==b )
print( a!=b )

print( 0 < a < 100 ) # True

print( 10 == a == 20 )

print( a>0 and a<100 )
print( a>0 or a<100 )

print( not a>0 )

print(7 & 4) #비트연산자

#a++ 증감 연산자 없음

a=10
a= a+3
print(a)

a+=3
print(a)

#b= a<10? 'A' : 'B' 삼항연산자 없음
b= 'A' if(a>10) else 'B'
print(b)

a= '10'
#print( a +3 )
print( int(a) + 3 ) #문자열을 인트로 바꿔줘.. 형변환

