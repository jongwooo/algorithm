#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int count[42] = {};
	int num;
	for (int i = 0; i < 10; i++) {
		cin >> num;
		count[num % 42]++;
	}
	int ans = 0;
	for (int c : count) {
		if (c > 0) ans++;
	}

	cout << ans;
}