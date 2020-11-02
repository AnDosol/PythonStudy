# dictionary : 사전 (타 언어의 Hash와 비슷한 구조)
# Key와 Value를 가지고 있는 한쌍의 자료구조
# ex) Key->baseball, value->야구

# 딕셔너리 사용법
# {Key1: value1, Key2: value2, Key3:Value3, ...}
'''
dic = {'name': 'pey', 'phone': '01011112222', 'birth': '1118'}
print(dic)
'''

'''
a = {1: 'hi'}
print(a[1])
b = {'a': [1,2,3]}
print(b)
print(b['a'][0])
'''

# 딕셔너리 쌍 추가
'''
a = {1: 'a'}
a[2] = 'b'
print(a)

a['neme']='pey'
print(a)
'''

# 딕셔너리 요소 삭제하기
'''
a = {2: 'b', 'name' : 'pey', 3: [1, 2, 3]}
print(a)
del a[2]
print(a)
a[1]='d'
print(a)
'''

# 딕셔너리를 사용하는 방법
# ex) 사람들 각각의 특기를 작성할때 편함
# {"김연아" : "피겨스케이팅", "류현진" : "야구"}
'''
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

b = {1: 'a', 2 : "b"}
print(b[1])
print(b[2])

c = {'a':1, 'b':2}
print(c['a'])
print(c['b'])

dic = {'name' : 'pey', 'phone' : '01011112222', 'birth' : '1212'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])
'''

# 딕셔너리를 만들때의 주의사항
'''
# 1.key는 고유한 값으로 중복되는 key값을 설정하면 하나를 제외한 나머지 값들은 무시가 된다.
a = {1: 'a', 1: 'b'}
print(a)
'''

# key에 리스트는 쓸수 없다.
# 하지만 튜플은 key로 쓸 수 있다.
# 딕셔너리의 key로 쓸수 있는지 없는지는 key가 변하는지 변하지 않는지에 달려있다
# 따라서 리스트는 값이 변하기 때문에 사용할수 없다
'''
#key에 리스트 사용시 에러
a = {[1,2] : 'hi'}
print(a)
a = {'a' : [1,2]}
print(a['a'])
'''

# 딕셔너리 관련 함수들
# key 리스트 만들기
'''
a = {'name':'pey', 'phone' : '01011112222', 'birth' : '1118'}
print(a.keys())

#키값들을 모두 확인하는법
for k in a.keys():
    print(k)
#키들을 리스트에 담는 방법
listA = list(a.keys())
print(listA)
print(listA[0])
'''

# value 리스트 만들기
'''
# .values() :  key 와 마찬가지로 value 를 얻기 위한 함수
a = {'name': 'pey', 'phone': '01011112222', 'birth': '1118'}
print(a.values())
c=list(a.values())
print(c)
'''

#Key,value 쌍 얻기
'''
a = {'name': 'pey', 'phone': '01011112222', 'birth': '1118'}
print(a.items())

c=list(a.items())
print(c)
print(c[0][0])
'''

#Key,Value 쌍 지우기
#.clear()
'''
a = {'name': 'pey', 'phone': '01011112222', 'birth': '1118'}
a.clear()
print(a)
'''

#Key로 Value 얻기2
#.get() : 없는 key 호출시 none 값을 돌려줌 -> a['nokey']의 경우는 에러발생
a = {'name': 'pey', 'phone': '01011112222', 'birth': '1118'}
print(a.get('nokey'))
print(a.get('birth'))
# print(a['nokey'])
print(a['birth'])

#딕셔너리 안에 찾으려는 key 값이 없을경우 디폴트(none)값이 아닌 다른 값을 가져오고 싶을때는
#get(x, '디폴트값')을 사용하면 편하다.

print(a.get('foo', 'bar'))
print(a.get('birth', 'bar'))

#해당 키가 딕셔너리 안에 있는지 조사하는 방법
#in : 있으면, true  없으면, false 반환
print('name' in a)
print('email' in a)
