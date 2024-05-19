﻿#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n) {
    int answer = 0;

    if (n % 2 == 0) {
        for (int i = 0; i < n + 1; i += 2) {
            answer += pow(i, 2);
        }
    }
    else {
        for (int i = 1; i < n + 1; i += 2) {
            answer += i;
        }
    }

    if (1 <= n <= 100) {
        return answer;
    }
}




// 다른 사람 풀이 

/* 
while (n > 0){
    answer += n % 2 == 0 ? n * n : n;
    n -= 2;
}
*/
