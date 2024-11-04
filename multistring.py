"""
날짜 : 2024/11/04
내용 : 파이썬 문자열 자료
"""


# 문자열 곱하기
print("=" * 50)
print("My program")
print("=" * 50)


# 문자열 길이 구하기
a = "Life is too short"
print(len(a))

#문자열 슬라이싱

print(a[:5])
print(a[8:])

# 문자열 포매팅
'''
포맷 코드
 - %s : 문자열(String)
 - %c : 문자1개(character)
 - %d : 정수(Integer)
 - %f : 부동소수(floating-point)
'''
# format() 메서드 사용 

name = "Alice"
age = 30
introduce = "My name is {} and i am {} years old" .format(name,age)
print(introduce)

# f-strings(Python 3.6 이상)
introduce2 = f"My name is {name} and i am {age} years old"
print(introduce2)

d={'name':'홍길동', 'age':23}
print(f"나는 {d["name"]}이고, 나이는{d["age"]}이다.")

#문자열 관련 함수

#count() :문자 개수 세기
print("a의 수 : ",introduce.count('a'))

#find() : 위치 알려주기(없을시 -1 리턴)
print("a가 가장 먼저 나온 위치 : ", introduce.find('a'))

#index() : 위치 알려주기 (없을시 오류)
print("index()로 a위치 찾기 : ", introduce.index('a'))

#join() : 문자열 삽입
print("abcd사이 \",\" 삽입하기 : ",",".join('abcd'))

#upper() : 소문자를 대문자로 바꾸기
print("대문자로 바꾸기 : ",name.upper())

#lower() : 대문자를 소문자로 바꾸기
print("소문자로 바꾸기 : ",name.lower())

#lstrip() : 왼쪽 공백 지우기
print("왼쪽 공백 지우기 : ",introduce.lstrip())

#rstip() : 오른쪽 공백 지우기
print("오른쪽 공백 지우기 : ",introduce.rstrip())

#strip() :양쪽 공백 지우기
print("양쪽 공백 지우기 : ",introduce.strip())

#replace() : 문자열 바꾸기
print("문자열 바꾸기 : ", a.replace("Life", "Your leg"))

#split() : 문자열 나누기
print("문자열 나누기 : ", a.split())
