#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	
	int n;
	int ans = 0;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		int sum = 0, num = i;
		while (num > 0) {
			sum += num % 10;
			num /= 10;
		}
		if (sum + i == n) {
			ans = i;
			break;
		}
	}
	cout << ans;
}