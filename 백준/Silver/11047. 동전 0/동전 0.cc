#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, k;
	cin >> n >> k;
	int a[11];
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	sort(a, a + n, greater<int>());
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		if (k >= a[i]) {
			cnt += k / a[i];
			k %= a[i];
		}
	}
	cout << cnt;
}