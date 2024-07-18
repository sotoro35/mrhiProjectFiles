#pyton 언어의 특징
# 1. 스크립트 인터프리터 언어
# 2. 동적타입 언어

#Ex01 화면 출력 print()

print(10)
print(3.14)
print(True)
print("Hello")

print(10, end="  ")
print(20)

a=15
print(a)

print(3+5)
print(3+3.14)

print("aa"+"bb")
#print("aa"+3) 숫자랑 문자열이랑 결합 불가

print("aa"+str(3)) #인트를 문자열로 바꿔달라 해야함

print(" {} 입니다".format(1000))
print( "{} + {} = {}".format(5,3,5+3))

print( f" {10} + {a} = {10+a}")

print(10,20,30,40)
print(10, "sam", True)
