#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    cin >> str;
    int length = str.length();
    if (1 <= length && length <= 10) {
        for (char ch : str)
            cout << (char)ch << endl;
    }
    else {
        cout << "error";
    }
    return 0;
}