'''
문제 설명:
문자열 my_string, overwrite_string과 정수 s가 주어집니다. 
문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
제한사항 :
my_string와 overwrite_string은 숫자와 알파벳으로 이루어져 있습니다.
1 ≤ overwrite_string의 길이 ≤ my_string의 길이 ≤ 1,000
0 ≤ s ≤ my_string의 길이 - overwrite_string의 길이
입력 : 
100
출력 : 
100 is even
'''

# def solution(my_string, overwrite_string, s):
#     answer = ''
#     return answer

def solution(my_string, overwrite_string, s):
    my_string = str(my_string)
    overwrite_string = str(overwrite_string)
    if 1 <= len(overwrite_string) <= len(my_string) <= 1000:
        if 0 <= s <= len(my_string) - len(overwrite_string):
            answer = my_string[:int(s)] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer