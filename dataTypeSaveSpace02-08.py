# 자료형의 값을 저장하는 공간, 변수

# 파이썬은 다른 언어와는 달리 변수에 저장된 값을 직접 판단하여 자료형을 선택해준다
'''
a = 1
b = "python"
c = [1, 2, 3]
'''

# 변수란?
'''
# 아래의 경우 [1,2,3]값을 가지는 리스트 자료형이 자동으로 메모리에 생성되고 변수 a는 [1,2,3]리스트가 저장된 메모리의 주소를 가르키게 된다.
a = [1, 2, 3]
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
'''

# 리스트를 복사하고자 할 때
'''
a = [1, 2, 3]
b = a11
# a에 있는값과 b에 있는 값이 동일함
print("a에 들어있는 값 : " + str(a))
print("b에 들어있는 값 : " + str(b))
# a주소와 b주소가 동일함
print("a id : " + str(id(a)))
print("b id : " + str(id(b)))
# a는b이다 = true
print(a is b)

#a[1]값을 바꿨더니 b의 값까지 같이 바뀜
a[1] = 4
print("a에 들어있는 값 : " + str(a))
print("b에 들어있는 값 : " + str(b))
'''

# 리스트를 복사하는 방법
'''
# 1. [:]
a=[1,2,3]
b=a[:]
a[1]=4
print("a의 값 : "+str(a))
print("b의 값 : "+str(b))
print("a의 주소 : "+str(id(a)))
print("b의 주소 : "+str(id(b)))
'''

# 2. copy 이용
'''
a = [1,2,3]
from copy import copy
b = copy(a)
print(b)
print(b is a)
print(id(a))
print(id(b))
'''

#변수를 만드는 여러가지 방법
'''
a, b = ('python', 'life')
print(a)
print(a[0])
print(a[1])
# 에러 발생
# a[2]=3
print(b)

# 아래와 a, b = ('python', 'life') 는동일
#(a,b)='python','life' 
'''
#리스트로 변수를 만드는법
'''
[a,b] = ['python','life']
print(a)
print(b)
'''

'''
a=b='python'
print(id(a))
print(id(b))
# 리스트와a=b와는 다르게 나타나는값이 상이함
a=3
print(a)
print(b)
'''

# 두변수의 값을 서로 바꾸는법
a,b=3,5
print("a의 값 : "+str(a)+"  /  b의 값 : " + str(b))
#서로 가지고 있는 변수값 바꾸기
a,b=b,a
print("a의 값 : "+str(a)+"  /  b의 값 : " + str(b))
