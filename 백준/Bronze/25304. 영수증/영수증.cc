#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int x, n, a, b;

	cin >> x;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		x -= a * b;
	}

	if (x == 0) cout << "Yes";
	else cout << "No";
}