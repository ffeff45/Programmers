'''
문제 설명:
자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.
제한사항 :
1 ≤ n ≤ 1,000
입력 : 
100
출력 : 
100 is even
'''

# a = int(input())

a = int(input())

if 1 <= a <= 1000:
    if a % 2 == 0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")
else:
    print("error")


# 다른 사람 풀이

n=int(input())
print(f"{n} is {'eovdedn'[n&1::2]}")

# 슬라이스 구문으로 a[ start : end : step ] ::step으로 2칸 씩 이동하면서 값이 가져오게 된다.