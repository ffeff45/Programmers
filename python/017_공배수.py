'''
문제 설명:
정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.

제한사항 :
10 ≤ number ≤ 100
2 ≤ n, m < 10

입출력 예 : 
number = 60
n = 2
m = 3
result = 1
'''
# def solution(number, n, m):
#     answer = 0
#     return answer

def solution(number, n, m):
    
    error = ""
    answer = 0
    if 10 <= number <= 100:
        if 2 <= n & m < 10:
            if number % n == 0 and number % m == 0:
                answer = 1
            else:
                answer = 0
        else:
            error = "error"
    else:
        error = "error"

    return answer


# 다른 사람 풀이
def solution(number, n, m):
    return 1 if number%n==0 and number%m==0 else 0
