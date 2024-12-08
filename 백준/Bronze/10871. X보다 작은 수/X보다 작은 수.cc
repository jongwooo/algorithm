#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, x;
	cin >> n >> x;

	int v;
	for (int i = 0; i < n; i++) {
		cin >> v;
		if (v < x) {
			cout << v << " ";
		}
	}
}