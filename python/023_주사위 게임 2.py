'''
문제 설명:
1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.
세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

제한사항 :
a, b, c는 1이상 6이하의 정수입니다.

입출력 예 : 
a = 2
b = 6
c = 1
result = 9  
'''

def solution(a, b, c):
    a,b,c = condition(a,b,c)
    s = {a,b,c}
    if len(s) == 1:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif len(s) == 2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return a+b+c

def condition(a,b,c):
    if 1 <= a <=6:
        x = a
    if 1 <= b <=6:
        y = b
    if 1 <= c <=6:
        z = c
    return x,y,z
    

print(solution(2,6,1))    
print(solution(5,3,3)) 
print(solution(4,4,4))

#다른 사람 풀이
# def solution(a, b, c):
#     check=len(set([a,b,c]))
#     if check==1:
#         return 3*a*3*(a**2)*3*(a**3)
#     elif check==2:
#         return (a+b+c)*(a**2+b**2+c**2)
#     else:
#         return (a+b+c)
