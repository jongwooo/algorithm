#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	cin >> t;
	while (t--) {
		int sum = 0;
		int min = 100;
		for (int i = 0; i < 7; i++) {
			int num;
			cin >> num;
			if (num % 2 == 0) {
				sum += num;
				if (num < min) min = num;
			}
		}
		cout << sum << ' ' << min << '\n';
	}
}