#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    cin >> str;
    for (int i = 0; i < str.size(); i++) {
        if ('a' <= str[i] && str[i] <= 'z') {
            str[i] -= 32;
        } else if ('A' <= str[i] && str[i] <= 'Z') {
            str[i] += 32;
        }
    }
    cout << str;
    return 0;
}