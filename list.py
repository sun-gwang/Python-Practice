"""
날짜 : 2024.11.04 (목)
내용 : 파이썬 리스트 자료형 학습
"""

# 리스트 자료형의 형태
odd = [1,3,5,7,9]
a = []
b = [1,2,3]
c = ['Life', 'is', 'too', 'short']
d = [1,2, 'Life', 'is']
e = [1,2,['Life','is']]
test = ['a','c','b']
print("리스트의 마지막 요소 가져오기 : ", b[-1])

print("리스트 요소 중 리스트의 요소 가져오기 : ", e[2][0])

print("리스트 슬라이싱 : ", c[:2])

print("리스트 크기 구하기 : ", len(c))

b[2] = 5
print("리스트 수정하기", b)

#del c[2]
print("del 함수로 요소 삭제하기 : ", c)

d.append("too")
print("append()함수로 요소 추가", d)


#문자열 정렬 순서 : 대문자 -> 알파벳 -> 유니코드 순서
c.sort()
print("sort함수로 정렬하기", c)

# pop()함수 : 리스트의 맨 마지막 요소를 삭제 후 리스트를 리턴한다.
odd.pop()
print("pop() 함수로 마지막 요소 삭제, 리턴 : ", odd)

print("리스트에 포함된 요소 (x)의 개수 세기",odd.count(3))

a.extend(b)
print("extend로 리스트 확장시키기 : ", a)
