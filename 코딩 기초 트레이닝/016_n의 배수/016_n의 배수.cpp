#include <string>
#include <vector>

using namespace std;

int solution(int num, int n) {
    int answer = int(not(num % n));

    if ((2 <= num <= 100) and (2 <= n <= 9)) {
        return answer;
    }

}