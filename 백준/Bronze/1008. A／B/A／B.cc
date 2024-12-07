#include <iostream>

using namespace std;

int main() {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    double A, B;
    cin >> A >> B;

    cout.precision(12);
    cout << fixed;
    cout << A / B;
}