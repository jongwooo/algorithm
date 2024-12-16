#include <iostream>
using namespace std;

typedef long long int lli;

int gcd(long long int a, lli b) {
	if (b == 0) return a;
	return gcd(b, a % b);
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	lli a, b;
	cin >> a >> b;
	cout << a * b / gcd(a, b);
}