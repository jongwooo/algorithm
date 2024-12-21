#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	cin >> t;
	while (t--) {
		int n, m;
		cin >> n >> m;
		int res = 1, tmp = 1;
		for (int i = m; i > m - n; i--) {
			res *= i;
			res /= tmp++;
		}
		cout << res << '\n';
	}
}