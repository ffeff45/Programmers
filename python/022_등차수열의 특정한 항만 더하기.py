'''
문제 설명:
두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다. 
첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때, 
이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.

제한사항 :
1 ≤ a ≤ 100
1 ≤ d ≤ 100
1 ≤ included의 길이 ≤ 100
included에는 true가 적어도 하나 존재합니다.

입출력 예 : 
a = 3
d = 4
included = [true, false, false, true, true]
result = 37
'''

def solution(a, d, included):
    a = condition_a(a)
    d = condition_d(d)
    included = condition_len(included)
    list_eq = []
    for i in range(len(included)):
        if included[i] == True:
            list_eq.append(a)
        a += d 
    answer = sum(list_eq)
    return answer  

def condition_a(a):
    if 1 <= a <= 100:
        return a
    else:
        ValueError

def condition_d(d):
    if 1 <= d <= 100:
        return d
    else:
        ValueError

def condition_len(included):
    if 1 <= len(included) <= 100:
        return included
    else:
        ValueError
    
print(solution(101,4,[True, False, False, True, True]))


#다른 사람 풀이 
# def solution(a, d, included):
#     answer = 0
#     for i in range(len(included)):
#         answer += (a + d * i) * int(included[i])
#     return answer