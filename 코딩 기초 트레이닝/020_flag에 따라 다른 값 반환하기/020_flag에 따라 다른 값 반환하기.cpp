#include <string>
#include <vector>

using namespace std;

int solution(int a, int b, bool flag) {
    int answer = 0;
    if (flag) {
        answer = a + b;
    }
    else {
        answer = a - b;
    }
    if ((-1000 <= a <= 1000) and (-1000 <= b <= 1000)) {
        return answer;
    }
}