#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	long s;
	cin >> s;
	long ans = 0;
	long start = 1; long end = s;
	while (start <= end) {
		long mid = (start + end) / 2;
		if (mid * (mid + 1) / 2 <= s) {
			ans = mid;
			start = mid + 1;
		}
		else {
			end = mid - 1;
		}
	}
	cout << ans;
}