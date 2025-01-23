#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		int digit = 0;
		while (n > 0) {
			if (n % 2 == 1) cout << digit << ' ';
			n /= 2;
			++digit;
		}
	}
}