#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b;
    cin >> a >> b;

    if (a > b) {
        cout << ">";
    } else if (a < b) {
        cout << "<";
    } else {
        cout << "==";
    }
}