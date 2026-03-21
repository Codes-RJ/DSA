#include <iostream>
#include <vector>
using namespace std;

int linearSearch(const vector<int>& values, int target) {
    for (int i = 0; i < static_cast<int>(values.size()); i++) {
        if (values[i] == target) {
            return i;
        }
    }
    return -1;
}

int main() {
    vector<int> values = {10, 20, 30, 40, 50};
    int target = 30;

    cout << "Array elements: ";
    for (int value : values) {
        cout << value << ' ';
    }
    cout << "\n";

    cout << "Index of " << target << ": " << linearSearch(values, target) << "\n";
    return 0;
}
