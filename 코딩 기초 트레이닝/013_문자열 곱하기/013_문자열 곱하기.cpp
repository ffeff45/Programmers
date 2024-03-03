#include <string>
#include <vector>

using namespace std;


string solution(string my_string, int k) {
    string answer = "";
    int size = my_string.size();
    string str;

    if (1 <= size && size <= 100) {
        for (int i = 0; i < size; i++) {
            if (islower(my_string[i]) != 0) {
                str += my_string[i];
            }
        }
    }
    else {
        answer = "error";
    }

    while (k--) {
        answer += str;
    }

    return answer;
}