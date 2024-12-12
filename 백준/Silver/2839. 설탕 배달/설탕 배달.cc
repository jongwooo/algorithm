#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	for (int i = 0; i <= n / 3; i++) {
		for (int j = 0; j <= n / 5; j++) {
			if (3 * i + 5 * j == n) {
				cout << i + j;
				return 0;
			}
		}
	}
	cout << -1;
}