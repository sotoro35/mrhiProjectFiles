def show():
    print("show function")

show()
show()

def output(a,b):
    print("a:",a)
    print("b:",b)

output(10,20)
#output(10) error

def output(a):
    print("오버로딩:", a)

output(10)

def display(a=1,b=2):
    print("a:",a)
    print("b:",b)

display(10,20)
display(10)
display()
display(b=5)


def nice( *values ): #가변길이 인자 .. 여러개를 전달
    print(len(values))
    for v in values:
        print(v)

nice()
nice(10)
nice(10,20)

def sum(a,b):
    return a+b

num= sum(5,3)
print(num)

def ccc():
    return 100,200,300

n1,n2,n3= ccc()
print(n1)
print(n2)
print(n3)

n=ccc()
print(n)


def eee(a):
    return a*10
print(eee(2))

fff= lambda a: a*10
print("fff:",fff(5))


#파이썬에는 여러 내장 함수가 존재함
file= open("aaa.txt","w")
file.write("This is python programming...")
file.close()

file= open("aaa.txt","r", encoding="UTF-8")
contents= file.read()
print("파일에서 읽어온 긁씨:",contents)
file.close()


    
