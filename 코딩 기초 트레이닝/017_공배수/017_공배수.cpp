#include <string>
#include <vector>

using namespace std;

int solution(int number, int n, int m) {
    int answer = (number % n == 0) and (number % m == 0) ? 1 : 0;
    if ((10 <= number <= 100) and (2 <= n <= 10) and (2 <= m <= 10)) {
        return answer;
    }
}