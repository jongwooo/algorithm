#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int a, b, c;
	cin >> a >> b >> c;

	if (a != b && b != c && c != a) {
		cout << max({ a, b, c }) * 100;
	}
	else if (a == b && b == c) {
		cout << 10000 + a * 1000;
	}
	else if (a == b || a == c) {
		cout << 1000 + a * 100;
	}
	else {
		cout << 1000 + b * 100;
	}
}