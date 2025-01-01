#include <iostream>
#include <string>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	string s;
	cin >> t;
	while (t--) {
		cin >> s;
		int sum = 0, cnt = 0;
		for (int i = 0; i < (int)s.size(); i++) {
			if (s[i] == 'O') cnt++;
			else cnt = 0;
			sum += cnt;
		}
		cout << sum << '\n';
	}
}