#배열

#파이썬은 배열이 없음. 대신 List, Tuple, dictionary
# 1. List
aaa= [10,20,30,40]
print(aaa)

print(aaa[0])
print(aaa[1])
print(aaa[2])

aaa[0]= 100
print(aaa)

aaa.append(50)
print(aaa)

aaa.insert(0,1000) #원하는 위치에 삽입
print(aaa)

aaa.remove(100) #100 숫자를 찾아 지워
print(aaa)

del aaa[2] # 2번방을 지워
print(aaa)

aaa.clear()  #전부 지워
print(aaa)

print('요소개수',len(aaa))

aaa= [10, 3.14, False, "sam"]
print(aaa)

for e in aaa :
    print(e)

aaa.reverse() #거꾸로
print(aaa)

aaa= [4,15,7,2,17,3,4,10]
aaa.sort()
print(aaa)

print( 7 in aaa )
print( 7 not in aaa )

print( aaa.count(4),"개" ) # 4라는 숫자가 몇개있니

print( aaa.pop(2) ) # 꺼내라는 의미
print (aaa )

aaa= [10,20,30]
bbb= [4,5,6]
aaa.extend(bbb) #concab처럼 뒤에 붙임
print(aaa)


#2. Tuple
bbb= (10,20,30)
print(bbb)
print(bbb[0])
print(bbb[1])
print(bbb[2])

#bbb[0] = 100 error 값변경 불가


#3. Dictionary
ccc= {"name":"sam", "age":20, "address":"seoul"}
print(ccc)

print( ccc['name'])
print( ccc['age'])
print( ccc['address'])

del ccc['address']
print(ccc)

for key in ccc : #key 값을 출력
    print(key)

for key in ccc: # 값을 출력
    print( ccc[key] )

print( type(aaa) )
print( type(bbb) )
print( type(ccc) )

