#include <iostream>
#include <cmath>
using namespace std;

const int RANGE = 2 * 123'456;
int nums[RANGE];

int main() {
	cin.tie(0)->sync_with_stdio(0);

	fill_n(nums, RANGE, 1);
	for (int i = 1; i <= RANGE; i++) {
		if (i == 1) continue;
		for (int j = 2; j <= (int)sqrt(i); j++) {
			if (i % j == 0) {
				nums[i] = 0;
				break;
			}
		}
	}
	int n;
	while (true) {
		cin >> n;
		if (n == 0) break;
		int cnt = 0;
		for (int i = n + 1; i <= 2 * n; i++) {
			cnt += nums[i];
		}
		cout << cnt << '\n';
	}
}