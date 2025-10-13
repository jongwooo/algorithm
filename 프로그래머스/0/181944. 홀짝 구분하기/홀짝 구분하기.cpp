#include <iostream>

using namespace std;

int main(void) {
    cin.tie(0) -> sync_with_stdio(0);
    int n;
    cin >> n;
    cout << n;
    if (n % 2 == 0) {
        cout << " is even";
    } else {
        cout << " is odd";
    }
    return 0;
}