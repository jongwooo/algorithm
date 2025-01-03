#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int m, n;
	int sum = 0, min = 10'001;
	cin >> m >> n;
	for (int i = 1; i * i <= n; i++) {
		if (i * i >= m) {
			sum += i * i;
			if (i * i < min) min = i * i;
		}
	}
	if (sum == 0) cout << -1;
	else cout << sum << '\n' << min;
}