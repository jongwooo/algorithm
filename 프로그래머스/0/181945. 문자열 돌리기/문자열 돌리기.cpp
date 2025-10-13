#include <iostream>
#include <string>

using namespace std;

int main(void) {
    cin.tie(0) -> sync_with_stdio(0);
    string str;
    cin >> str;
    for (int i = 0; i < str.size(); i++) {
        cout << str[i] << '\n';
    }
    return 0;
}