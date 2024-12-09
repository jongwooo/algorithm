#include <iostream>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int t;
	string s;

	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> s;
		cout << s[0] << s[s.length() - 1] << '\n';
	}
}