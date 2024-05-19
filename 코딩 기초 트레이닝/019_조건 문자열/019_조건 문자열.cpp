#include <string>
#include <vector>

using namespace std;

int solution(string ineq, string eq, int n, int m) {
    int answer = 0;
    if (eq == "=") {
        answer = (ineq == "<") ? int(n <= m) : int(n >= m);
    }
    else {
        answer = (ineq == "<") ? int(n < m) : int(n > m);
    }

    if ((1 <= n <= 100) and (1 <= m <= 100)) {
        return answer;
    }
}