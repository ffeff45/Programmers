'''
문제 설명:
문자열 str이 주어집니다.
문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.
제한사항 :
1 ≤ str의 길이 ≤ 10
입출력 예:
입력 : 
abcde
출력 : 
a
b
c
d
e
'''

# str = input()

str = input()

if 1<= len(str) <= 10:
        for i in str:
            print(i)
else:
    print("error")