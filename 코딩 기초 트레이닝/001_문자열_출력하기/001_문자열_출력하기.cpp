#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    cin >> str;
    int length = str.length();
    if (length >= 1 && length <= 1000000)
    {
        for (int i = 0; i < length; i++) {
            if (isspace(str[i]) == 0) {
                cout << str[i];
            }
        }
    }
    return 0;
}