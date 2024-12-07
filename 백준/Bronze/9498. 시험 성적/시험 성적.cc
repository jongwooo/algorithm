#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int score;
    cin >> score;

    if (90 <= score) {
        cout << "A";
    } else if (80 <= score) {
        cout << "B";
    } else if (70 <= score) {
        cout << "C";
    } else if (60 <= score) {
        cout << "D";
    } else {
        cout << "F";
    }
}