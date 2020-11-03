# 불 자료형
#https://kr.mathworks.com/videos/arduino-support-in-simulink-117736.html?s_tid=srchtitle
# 참 거짓
'''
a = True
b = False

print(type(a))
print(type(b))

print("True : " + str(1 == 1))
print("False : " + str(2 == 1))

# 자료형의 참과 거짓
# "python" : 참
# "" : 거짓
# [1,2,3] : 참
# [] : 거짓
# () : 거짓
# {} : 거짓
# 1 : 참
# 0 : 거짓
# None : 거짓

if "python":
    print("python : "+"참")
else :
    print("python : "+"거짓")

if "":
    print('"" : '+"참")
else :
    print('"" : '+"거짓")

if [1,2,3]:
    print("[1,2,3] : "+"참")
else :
    print("[1,2,3] : "+"거짓")

if []:
    print("[] : "+"참")
else :
    print("[] : "+"거짓")

if ():
    print("() : "+"참")
else :
    print("() : "+"거짓")

if {}:
    print("{} : " + "참")
else :
    print("{} : " + "거짓")

if 1 :
    print("1 : " + "참")
else :
    print("1 : " + "거짓")

if 0 :
    print("0 : " + "참")
else :
    print("0 : " + "거짓")

if None :
    print("None : "+ "참")
else :
    print("None : "+ "거짓")
'''

# 비어있는 문자열, 리스트 , 튜플, 딕셔너리 등의 값( "", [], (), {} )이 비어 있으면, false
# None -> False
'''
# 참과 거짓의 예
a = [1, 2, 3, 4]
i = len(a)-1
# pop() is an inbuilt function in Python that removes and returns last value from the list or the given index value.
while a:
    print(str(i) + "번째 값 : " + str(a.pop()))
    i -= 1

if []:
    print("참")
else :
    print("거짓")
'''

print("bool(python) : " + str(bool('python')))
print('bool("") : ' + str(bool("")))
print('bool([1,2,3]) : ' +str(bool([1,2,3])))
print('bool([]) : ' + str(bool([])))
print('bool(0) : ' +str(bool(0)))
print('bool(3) : ' +str(bool(3)))