#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int t, a, b;
	cin >> t;

	for (int i = 1; i <= t; i++) {
		cin >> a >> b;
		cout << "Case #" << i << ": " << a + b << '\n';
	}
}