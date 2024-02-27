'''
문제 설명:
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.

단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.

제한사항 :
1 ≤ a, b < 10,000

입출력 예 : 
a = 9
b = 91
result = 991
'''

# def solution(a, b):
#     answer = 0
#     return answer

def solution(a, b):
    ab1 = int(str(a) + str(b))
    ab2 = int(str(b) + str(a))
    if 1 <= a & b < 10000:
        if ab1 < ab2:
            answer = ab2
        else:
            answer = ab1
    return answer


#다른 사람 풀이 + 내가 수정
def solution(a, b):
    if 1 <= a & b < 10000:
        answer = max(int(f"{a}{b}"),int(f"{b}{a}"))
    return answer