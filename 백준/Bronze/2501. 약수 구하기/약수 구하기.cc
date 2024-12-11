#include <iostream>
#include <vector>
using namespace std;

int n, k;
vector<int> factors;
int cnt = 0;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> n >> k;
	for (int i = 1; i <= n; i++) {
		if (n % i == 0) {
			factors.push_back(i);
			cnt++;
		}
	}
	if (cnt < k) cout << 0;
	else cout << factors[k - 1];
	return 0;
}