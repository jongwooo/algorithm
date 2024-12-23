#include <iostream>
using namespace std;

long factorial(long x) {
	if (x == 0) return 1;
	return x * factorial(x - 1);
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	cout << factorial(n);
}