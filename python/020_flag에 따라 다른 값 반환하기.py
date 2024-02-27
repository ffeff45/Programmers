'''
문제 설명:
두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, 
flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.

제한사항 :
-1,000 ≤ a, b ≤ 1,000

입출력 예 : 
a = -4
b = 7
flag = true
result = 3
'''

# def solution(a, b, flag):
#     answer = 0
#     return answer

def solution(a, b, flag):
    a = condition_a(a)
    b = condition_b(b)
    if flag == True:
        return a + b
    elif flag == False:
        return a - b

    
def condition_a(a):
    if -1000 <= a:
        return a
    
def condition_b(b):
    if b <= 1000:
        return b
        

print(solution(-4,7,True))