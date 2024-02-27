'''
문제 설명:
정수 a와 b가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.
제한사항 :
-100,000 ≤ a, b ≤ 100,000
입출력 예:
입력 : 4 5
출력 : a = 4, b = 5
'''


# a, b = map(int, input().strip().split(' '))
# print(a + b)

a, b = map(int, input().strip().split(' '))

if -100000 <= a & a <= 100000:
    if -100000 <= b & b <= 100000:
        print("a = "+str(a))
        print("b = "+str(b))
else:
     print("error") 