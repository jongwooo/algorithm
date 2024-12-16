#include <iostream>
using namespace std;

int gcd(int a, int b) {
	if (a % b == 0) return b;
	return gcd(b, a % b);
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int a, b;
		cin >> a >> b;
		cout << a * b / gcd(a, b) << '\n';
	}
}