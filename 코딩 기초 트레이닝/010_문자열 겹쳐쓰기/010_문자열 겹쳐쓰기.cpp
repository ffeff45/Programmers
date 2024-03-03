#include <string>
#include <vector>

using namespace std;

string solution(string my_string, string overwrite_string, int s) {
    string answer = "";
    int my_string_l = my_string.length();
    int overwrite_string_l = overwrite_string.length();

    if (1 <= my_string_l <= overwrite_string_l <= 1000) {
        if (0 <= s <= my_string_l - overwrite_string_l) {
            answer = my_string.replace(s, overwrite_string_l, overwrite_string);
        }
        else {
            answer = "error";
        }
    }
    else {
        answer = "error";
    }

    return answer;
}