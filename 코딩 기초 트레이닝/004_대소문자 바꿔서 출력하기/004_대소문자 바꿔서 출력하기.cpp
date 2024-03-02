#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    cin >> str;

    int length = str.length();

    if (1 <= length && length <= 20) {
        for (int i = 0; i < str.size(); i++) {
            if (isupper(str[i])) {
                str[i] = tolower(str[i]);
            }
            else if (islower(str[i])) {
                str[i] = toupper(str[i]);
            }
        }
    }
    cout << str << endl;
    return 0;
}