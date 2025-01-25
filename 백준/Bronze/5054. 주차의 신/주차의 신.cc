#include <iostream>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int min = 100, max = -1;
        for (int i = 0; i < n; i++) {
            int input;
            cin >> input;
            if (input < min) min = input;
            if (max < input) max = input;
        }
        cout << (max - min) * 2 << '\n';
    }
}