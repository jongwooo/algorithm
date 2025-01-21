#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int idx;
	int sum = 0;
	for (int i = 1; i <= 5; i++) {
		int a, b, c, d;
		cin >> a >> b >> c >> d;
		if (sum < a + b + c + d) {
			idx = i;
			sum = a + b + c + d;
		}
	}
	cout << idx << ' ' << sum;
}
