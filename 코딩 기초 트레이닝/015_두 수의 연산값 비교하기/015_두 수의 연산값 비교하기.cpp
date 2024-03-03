#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    int answer = 0;
    int ab1 = stoi(to_string(a) + to_string(b));
    int ab2 = 2 * a * b;

    if (1 <= a == b <= 10000) {
        answer = max(ab1, ab2);
    }

    return answer;
}