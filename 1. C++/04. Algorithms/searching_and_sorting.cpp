#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int binarySearch(const vector<int>& values, int target) {
    int left = 0;
    int right = static_cast<int>(values.size()) - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (values[mid] == target) {
            return mid;
        }
        if (values[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

int main() {
    vector<int> values = {9, 4, 7, 1, 3};
    sort(values.begin(), values.end());

    cout << "Sorted values: ";
    for (int value : values) {
        cout << value << ' ';
    }
    cout << "\n";

    cout << "Binary search result for 7: " << binarySearch(values, 7) << "\n";
    return 0;
}
