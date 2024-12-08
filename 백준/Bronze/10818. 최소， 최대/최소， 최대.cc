#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	cin >> n;
	int minValue, maxValue;
	minValue = 1000000;
	maxValue = -1000000;

	int v;
	for (int i = 0; i < n; i++) {
		cin >> v;
		if (v < minValue) {
			minValue = v;
		}
		if (maxValue < v) {
			maxValue = v;
		}
	}

	cout << minValue << " " << maxValue;
}