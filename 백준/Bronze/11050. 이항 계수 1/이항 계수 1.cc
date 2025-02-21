#include <iostream>
using namespace std;

int factorial(int x) {
	if (x == 0) return 1;
	return x * factorial(x - 1);
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, k;
	cin >> n >> k;
	cout << factorial(n) / (factorial(n - k) * factorial(k));
}