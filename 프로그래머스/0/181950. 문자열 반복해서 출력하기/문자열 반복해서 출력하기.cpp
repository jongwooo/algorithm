#include <iostream>
#include <string>

using namespace std;

int main(void) {
    cin.tie(0)->sync_with_stdio(0);
    string str;
    int n;
    cin >> str >> n;
    while (n--) {
        cout << str;
    }
    return 0;
}