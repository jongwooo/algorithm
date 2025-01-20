#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	cin >> t;
	while (t--) {
		int n;
		char str[81];
		cin >> n >> str;
		for (int i = 0; str[i] != '\0'; i++) {
			if (i == n - 1) continue;
			cout << str[i];
		}
		cout << '\n';
	}
}