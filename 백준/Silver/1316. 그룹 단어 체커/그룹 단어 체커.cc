#include <iostream>
#include <string>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	
	int n;
	string s;

	cin >> n;

	int count = 0;
	for (int i = 0; i < n; i++) {
		cin >> s;
		if (s.length() <= 2) continue;
		for (int j = 0; j < s.length() - 1; j++) {
			if (s[j] == s[j + 1]) continue;
			if (s.find(s[j], j + 2) != string::npos) {
				count++;
				break;
			}
		}
	}

	cout << n - count;
}