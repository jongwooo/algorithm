#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, m;
	int basket[101] = { 0, };
	int i, j, k;

	cin >> n >> m;
	for (int a = 0; a < m; a++) {
		cin >> i >> j >> k;
		for (int b = i; b <= j; b++) {
			basket[b] = k;
		}
	}

	for (int a = 1; a <= n; a++) {
		cout << basket[a] << " ";
	}
}