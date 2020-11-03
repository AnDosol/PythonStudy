'''
홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자
국어 : 80
영어 : 75
수학 : 55
'''
'''
average= {'name' : "홍길동", "english" : 75, "korean" : 80, "math" : 55}
ans = average["english"] + average["korean"] + average["math"] /(len(average)-1)
print(ans)
'''

'''
자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.
'''
'''
Q2 = {"number": 13}
# Q2["number"]=1
# Q2["number"]=2
if Q2["number"] % 2 == 1:
    print('홀수')
else:
    print('짝수')
'''

'''
홍길동 씨의 주민등록번호는 881120-1068234이다.
홍길동 씨의 주민등록번호를 연월일(YYYYMMDD)부분과 그 뒤의 숫자 부분으로 나누어 출력해보자
'''

'''
idenNum = {"홍길동" : "881120-1068234"}
print("주민등록번호 앞 : "+idenNum["홍길동"][:6])
print("주민등록번호 뒤 : "+idenNum["홍길동"][7:])
print("성별 : " + idenNum["홍길동"][7])
a= "a:b:c:d"
'''

'''
다음과 같은 문자열 a:b:c:d 가 있다. 문자열의 replace함수를 사용하여 a#b#c#d로 바꿔서 출력해보자
a= "a:b:c:d"
'''

'''
a = "a:b:c:d"
print(a)
a=a.replace(":", "#",1)
print(a)
a=a.replace(":", "#")
print(a)
'''

'''
[1,3,5,4,2]를 [5,4,3,2,1]로 변경
'''

