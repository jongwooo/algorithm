#include <iostream>
#include <string>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	cin >> t;
	while (t--) {
		int a, b;
		cin >> a >> b;
		int cnt = 0;
		for (int i = a; i <= b; i++) {
			string s = to_string(i);
			for (int j = 0; s[j] != '\0'; j++) {
				if (s[j] == '0') cnt++;
			}
		}
		cout << cnt << '\n';
	}
}