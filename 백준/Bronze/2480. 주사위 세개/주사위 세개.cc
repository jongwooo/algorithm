#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int a, b, c;
	cin >> a >> b >> c;
	if (a != b && b != c && c != a) {
		cout << max({ a, b, c }) * 100;
	}
	else if (a == b && b == c) {
		cout << 10'000 + a * 1'000;
	}
	else if (a == b || a == c) {
		cout << 1'000 + a * 100;
	}
	else {
		cout << 1'000 + b * 100;
	}
}