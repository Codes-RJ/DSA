#include <iostream>
using namespace std;

int main() {
    int n = 5;

    cout << "Numbers from 1 to " << n << ":\n";
    for (int i = 1; i <= n; i++) {
        cout << i << ' ';
    }
    cout << "\n";

    cout << "Even or odd check:\n";
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            cout << i << " is even\n";
        } else {
            cout << i << " is odd\n";
        }
    }

    return 0;
}
