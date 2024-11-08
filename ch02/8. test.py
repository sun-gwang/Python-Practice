"""
날짜 : 2024.11.05
내용 : 2장 되새김 문제
"""

"""
    1. 홍길동 씨의 과목별 줌스는 다음과 같다. 홍길동씨의 평균 점수를 구해보자.
    국어 80, 영어 75, 수학 55

"""
korean = 80
english = 75
math = 55

avg = (korean + english + math)/3
print("홍길동의 평균 : ", avg)


"""
    2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법은?
"""

if 13%2 ==0 :
    print("짝수입니다.")
else :
    print("홀수입니다.")
    

"""
    3. 홍길동씨의 주민등록번호는 881120-1068234이다. 홍길동씨의 주민등록번호를
    연월일(YYMMDD) 부분과 그 뒷부분으로 나누어 출력해보자

"""
pinNum = "881120-1068234"


print("홍길동씨의 생년월일 : ", pinNum[:6])
print("홍길동씨의 뒷자리 번호 : ", pinNum[7:])


"""
    4. 주민등록번호 뒷자리의 맨 첫쨰 숫자는 성별을 나타낸다.
    주민등록번호에서 성별을 나타내는 숫자를 출력해보자.
"""
genCode = pinNum.split("-")[1][0]
print("성별 : ", genCode)


"""
    5. 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여
    a#b#c#d로 바꿔서 출력해보자.
"""
exam5 = "a:b:c:d"

answer5 = exam5.replace(":","#")
print("replace()함수로 문자열 재배치 : ", answer5)


"""
    6. [1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들어보자.
"""
exam6 = [1,3,5,4,2]
exam6.sort()
exam6.reverse()
print("6번 답 : ", exam6)


"""
    7. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해보자.
"""
exam7 = ['Life', 'is', 'too', 'short']
answer7 = " ".join(exam7)
print("7번 답 : ", answer7)


"""
    8.(1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해보자.

    해답 1 (내가 푼 방식)
    튜플 -> 리스트 -> 리스트에 요소 추가 -> 다시 튜플로

    해답 2
    튜플b=(4)를 선언
    a+b
"""
exam8 = (1,2,3)
list8 = list(exam8)
list8.append(4) 
asnwer8 = tuple(list8)
print("8번답", asnwer8)

exam8_1 = (1,2,3)
exam8_b = (4,) #하나의 요소를 가진 튜플로 정의하려면 ,를 붙여야함.
answer8_1 = exam8_1+exam8_b
print("8번답 2 : ", answer8_1)


"""
    9. a리스트에서 중복 숫자를 제거해보자.
    a_9 = [1,1,1,2,2,3,3,4,4,5]
"""
a_9 = [1,1,1,2,2,3,3,4,4,5]

answer9 = list(set(a_9))
print("9번 답 : ", answer9)


"""
    파이썬은 다음처럼 동일한 값에 여러가지 변수를 선언할 수 없다.
    다음과 같이 a,b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b의 값은 어떻게 될까?
    그리고 이런 결과가 오는 이유에 대해 설명해보자.

    a = b = [1,2,3]
"""
# 정답 : b의 값도 변경된다? -> 같은 주소에 매핑되기 때문
