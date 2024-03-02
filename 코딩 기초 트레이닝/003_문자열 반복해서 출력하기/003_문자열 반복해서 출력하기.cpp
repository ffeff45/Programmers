#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    int n;
    cin >> str >> n;
    while (n--) {
        cout << str;
    }

    //     int length = str.length();
    //     if(1 <= length && length <= 10){
    //         if(1 <= n && n <=5){
    //            while(n--){
    //                 cout << str;
    //             }

    //         }
    //         else{
    //             cout << "error";
    //         }
    //     }
    //     else{
    //         cout << "error";
    //     }
    return 0;
}