#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str1, str2;
    cin >> str1 >> str2;
    int length1 = str1.length();
    int length2 = str2.length();
    if (1 <= length1 && length1 <= 10) {
        if (1 <= length2 && length2 <= 10) {
            cout << str1 + str2;
        }
    }
    return 0;
}