#include <iostream>
using namespace std;

int gcd(int i, int j) {
	if (j == 0) return i;
	return gcd(j, i % j);
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int a, b;
	cin >> a >> b;
	cout << gcd(a, b) << '\n' << a * b / gcd(a, b);
}