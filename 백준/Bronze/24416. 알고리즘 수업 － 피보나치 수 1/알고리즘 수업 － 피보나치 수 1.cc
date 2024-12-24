#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	int tmp, a = 1, b = 1;
	for (int i = 3; i <= n; i++) {
		tmp = b;
		b += a;
		a = tmp;
	}
	cout << b << ' ' << n - 2;
}