#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int sum = 0;
	int min = 100;
	for (int i = 0; i < 7; i++) {
		int n;
		cin >> n;
		if (n % 2 == 0) continue;
		if (n < min) min = n;
		sum += n;
	}
	if (sum == 0) cout << -1;
	else cout << sum << '\n' << min;
}