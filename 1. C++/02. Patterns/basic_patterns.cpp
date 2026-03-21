#include <iostream>
using namespace std;

int main() {
    int rows = 5;

    cout << "Right triangle pattern:\n";
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "* ";
        }
        cout << "\n";
    }

    cout << "\nNumber pattern:\n";
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            cout << j << ' ';
        }
        cout << "\n";
    }

    return 0;
}
