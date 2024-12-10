#include <iostream>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	string s;
	getline(cin, s);

	if (s.length() == 1 && s[0] == ' ') {
		cout << 0;
		return 0;
	}

	int ans = 1;
	for (int i = 1; i < s.length() - 1; i++) {
		if (s[i] == ' ') ans++;
	}
	cout << ans;
}