#include <iostream>
#include <string>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	string s;
	cin >> s;

	for (int i = 0; i < s.length() / 2; i++) {
		if (s[i] != s[s.length() - i - 1]) {
			cout << 0;
			return 0;
		}
	}
	cout << 1;
}