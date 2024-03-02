#include <iostream>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    if (1 <= n && n <= 1000) {
        cout << n << " is " << (n % 2 == 0 ? "even" : "odd");
    }
    return 0;
}