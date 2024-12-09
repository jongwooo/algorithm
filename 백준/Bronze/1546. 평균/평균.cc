#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	int m = -1;
	double sum = 0;

	cin >> n;

	double v;
	for (int i = 0; i < n; i++) {
		cin >> v;
		sum += v;
		if (m < v) {
			m = v;
		}
	}
	cout << ((sum / m) / n) * 100;
}