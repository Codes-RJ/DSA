#include <iostream>
#include <vector>
using namespace std;

int maxWindowSum(const vector<int>& values, int k) {
    if (k > static_cast<int>(values.size())) {
        return 0;
    }

    int windowSum = 0;
    for (int i = 0; i < k; i++) {
        windowSum += values[i];
    }

    int best = windowSum;
    for (int i = k; i < static_cast<int>(values.size()); i++) {
        windowSum += values[i] - values[i - k];
        if (windowSum > best) {
            best = windowSum;
        }
    }
    return best;
}

int main() {
    vector<int> values = {2, 1, 5, 1, 3, 2};
    cout << "Maximum sum of window size 3: " << maxWindowSum(values, 3) << "\n";
    return 0;
}
