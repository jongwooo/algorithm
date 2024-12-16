#include <iostream>
using namespace std;

int gcd(int a, int b) {
	if (b == 0) return a;
	return gcd(b, a % b);
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int a1, a2, b1, b2;
	cin >> a1 >> a2 >> b1 >> b2;
	int c1 = a1 * b2 + b1 * a2;
	int c2 = a2 * b2;
	cout << c1 / gcd(c1, c2) << ' ' << c2 / gcd(c1, c2);
}