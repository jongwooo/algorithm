#include <iostream>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	
	const int coins[4] = { 25, 10, 5, 1 };
	int t, c;

	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> c;
		for (int i = 0; i < 4; i++) {
			cout << c / coins[i] << ' ';
			c %= coins[i];
		}
	}
}