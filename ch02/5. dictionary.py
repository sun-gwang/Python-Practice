"""
날짜 : 2024.11.04
내용 : 딕셔너리 자료형 학습
"""

"""
    자바의 map 처럼 key-value 형태를 가지는 자료형으로,
    연관배열(associative array) 또는 해시(hash)라고 부른다.

    딕셔너리(해쉬)는 리스트나 튜플처럼 순차적으로 요솟값을 구하지 않고,
    key를 통해 value를 얻는다. 특정 값을 찾기위해 모든 내용을 순차적으로 찾지 않고,
    해당 단어(key)가 있는 곳만 찾는다.

    주의점
    1. key가 중복되도록 값을 입력하면 하나를 제외한 나머지 값들이 모두 무시된다.
    2. key에 리스트를 쓸 수 없다. key값은 변하지 않는(immutable) 값이어야 한다.(튜플은 사용 가능)
    
    
"""

# 기본 딕셔너리 형태
dic = {'name': 'pey', 'phone':'010-9999-1234', 'birth':'1115'}

a = {1:'a'}

#a[key] = value
a[2] = 'b'
print("딕셔너리 쌍 추가하기 : ", a)

#del dic[key]
del dic['birth']
print("딕셔너리 요소 삭제하기", dic)

"""
    파이썬 2.7버전 까지는 리스트로 key, value값들을 리턴했는데,
    메모리 낭비가 크다 보니 dict_key, dict_values 객체를 리턴하도록 변경되었다.
    리스트로 가져오고 싶을 경우 list(dic.keys()), list(dic.values()), list(dic.items())
    의 형태로사용하면 된다.
"""

print("keys() 함수로 key 값들 객체로  가져오기 : ", dic.keys())

print("keys()함수로 key값들 리스트로 가져오기 : ", list(dic.keys()))

print("values() 함수로 value 값들 객체로 가져오기 : ", dic.values())

print("values() 함수로 value 값들 리스트로 가져오기 : ", list(dic.values()))

print("items() 함수로 key, value값들 모두 객체로 가져오기 : ", dic.items())

print("items() 함수로 key, value 값들 모두 리스트로 가져오기 : ", list(dic.items()))


a.clear()
print("clear() 함수로 key:value 쌍 모두 지우기 : ", a)

"""
    dic[key]와 dic.get(key)의 차이
    
    dic[key]는 해당 key 값이 없을 경우 오류를 발생한다.
    dic.get(key)는 값이 없을 경우 None읠 리턴한다.
"""
print("get('key') 함수로 key값으로 value 가져오기 : ", dic.get('phone'))

print("get() 함수로 존재하지 않는 키 넣어보기 : ", dic.get('noneKey'))

# print("일반 방식으로 존재하지 않는 키 넣어보기 : ", dic['nonKey'])

print("일치하는 key가 없을 경우 미리 정해둔 값 리턴하기 : ", dic.get('noKey', "없습니다."))

print("in() 함수로 해당 key가 dict 안에 있는지 조사하기 : ", 'phone' in dic)
