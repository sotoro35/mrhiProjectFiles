# 자료형의 종류
# 1. 기본자료형 : int, float, str, bool
# 2. 배열(컬렉션) 자료형 : list, tuple, dict
# 3. None : nothing

#변수 선언 - 그냥 변수명 = 대입연산자로 값을 대입하면 됨
a= 10
print(a)

b=5.5
print(b)

c= False
print(c)

d= "sam"
print(d)

e= 'robin'
print(e)

f= None
print(f)

print( type(a) )
print( type(b) )
print( type(c) )
print( type(d) )
print( type(e) )
print( type(f) )

a= "Hello"
print(a)
print( type(a) )

# 대입연산자에 2개 이상의 값도 대입이 가능함
a,b = 10,20
print(a,b)

# a,b = 100 error 변수의 갯수만큼 값도 갯수가 맞아야 함

a= 100,200 #tuple타입으로 저장됨
print(a)
print( type(a) )
print ( a[0] )
print ( a[1] )

# 문자열 관련 연산자들..
print("aa" + "bb") #결합 연산자
print("aa" * 3 ) #반복 연산자
s = "Hello" * 5
print(s)

# 문자열 인덱싱 -- 일종의 substr
print( "Hello world" [1])
print( "Hello world" [1:7]) # 1부터 7번전까지
print( "Hello world" [1:]) # 1부터 끝까지
print( "Hello world" [:7]) # 0부터 6번까지
print( "Hello world" [-1]) # 뒤에서 첫번째
print( "Hello world" [-5:])

# 문자열의 길이 len()
s= "android"
print( len(s) )

# 문자열의 주요메소드들()
print("{}원".format(50000))
print("Hello".upper())
print("Hello".lower())
print("     Hello    ", "@@")
print("     Hello    ".strip(),"@@")

print("Hello world, android, ios, android".find('world'))

csv= "sam,20,seoul".split(",")
print(csv)
print( type(csv) )
print(csv[0])
print(csv[1])
print(csv[2])

print("world" in "Hello world") #True

print('''안녕하세요.
반가워요''')

"""여러줄
주석
입니다
"""
