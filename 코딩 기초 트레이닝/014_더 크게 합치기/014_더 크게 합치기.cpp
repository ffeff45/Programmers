#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    int answer = 0;
    string ab = to_string(a) + to_string(b);
    string ba = to_string(b) + to_string(a);

    if (1 <= a == b <= 10000) {
        answer = max(stoi(ab), stoi(ba));
    }

    return answer;
}