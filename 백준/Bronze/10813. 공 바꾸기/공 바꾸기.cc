#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, m;
	int basket[101] = { 0, };
	int i, j;

	cin >> n >> m;
	for (int a = 1; a <= n; a++) {
		basket[a] = a;
	}
	for (int a = 0; a < m; a++) {
		cin >> i >> j;
		swap(basket[i], basket[j]);
	}

	for (int a = 1; a <= n; a++) {
		cout << basket[a] << " ";
	}
}