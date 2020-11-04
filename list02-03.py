# 리스트는 muttable 하다~!
# 튜플과 가장 큰 차이라고 할 수 있지!
# 리스트 학습 https://wikidocs.net/14

'''
odd = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = []
b = [1, 2, 3]
c = ['life', 'is']
d = [1,2,'life','is']
e = [1,2,['life','is']]

print(a)
print(b)
print(c)
print(d)
print(e)

print("test : "+e[2][0])
print(d[0]+d[1])
#b의 마지막 값
print(b[-1])
print(e[-1][0])
'''

''' #리스트의 슬라이싱
a = "12345"
print(a[0:2])
b = a[:2]
c = a[2:]
print("b : "+ b)
print("c : "+ c)

d = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(d)
print(d[3][-1])
'''

# 리스트 연산하기
# 아래 결과는 "abc"+"def" = "abcdef" 와 비슷함.
'''
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
'''

# 리스트 반복하기
'''
a = [1, 2, 3]
a = a * 3
print(a)
'''

# 리스트 길이구하기
'''
a = [1, 2, 3]
print(len(a))
'''

# 문자와 숫자 같이 출력하는법
'''
a = [1, 2, 3]
# 아래와 같은 문자열+숫자 형식은 에러가 발생한다.
# 숫자와 문자 타입의 자료형은 더할수 없기 때문이다.
# print(a[2] + "hi")
# 만약, 숫자와 문자열을 같이 출력하고 싶다면,
# str()함수를 사용하면 된다.
print(str(a[2])+" hi")
'''

# 리스트의 수정과 삭제
'''
a = [1,2,3]
print(a)
#2번 인덱스의 값 바꾸기
a[2]=4
print(a)
'''

# del 함수 사용해서 리스트 요소 삭제하기
# del 함수는 파이썬이 자체적으로 가지고 있는 삭제 함수이다.
# 객체란 파이썬에서 사용되는 모든 자료형을 말한다.
'''
a = [1,2,3]
del a[1]
print(a)

b = [1,2,3,4,5]
del b[2:]
print(b)
'''

# 리스트 관련 함수들
# .append() : 리스트의 맨 마지막에 x를 추가하는 함수
'''
a = [1, 2, 3]
a.append(4)
print(a)
#아래 예시는 리스트를 추가한것이다.
#리스트 안에는 어떠한 자료형도 추가할 수 있다.
a.append([5, 6])
print(a)
'''

# 리스트 정렬(sort)
# sort함수는 리스트의 요소를 순서대로 정렬해준다.
'''
a = [1, 4, 3, 2]
a.sort()
print(a)
'''

# 리스트 뒤집기(reverse)
# reverse 함수는 현재 리스트의 요소를 역순으로 뒤집는다(순서를 다시 정렬해서 뒤집지 않음)
'''
a = ['a','c','b']
a.reverse()
print(a)
'''

# 위치 반환(index)
'''
a = [1,2,3]
#해당하는 값이 있으면 위치값을 return한다
print(a.index(3))
print(a.index(1))
'''

# 리스트에 요소 삽입(insert)
'''
# .insert(a, b) : 리스트의 a번째 위치에 b를 삽임하는 함수이다
a = [1, 2, 3]
# 0번 자리에 4를 입력
a.insert(0, 4)
print(a)
'''

# 리스트 요소 제거(remove)
'''
# .remove(x) : 리스트 중 첫번째 x값을 제거
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
# 3을 한번 더 지우면 두번째 3이 삭제 됨
a.remove(3)
print(a)
'''

# 리스트 요소 끄집어내기(pop)
'''
# .pop : 마지막 요소는 돌려주고 그 요소는 삭제한다.
a = [1,2,3]
a.pop()
print(a)
'''

# 리스트 확장(extend)
'''
# .extend(x) : a리스트에 x리스트를 더한다. x는 오직 리스트만 가능
a = [1,2,3]
a.extend([4,5])
print(a)
#extend는 +=[x, ...]과 동일
a +=[4,5]
print(a)
'''




