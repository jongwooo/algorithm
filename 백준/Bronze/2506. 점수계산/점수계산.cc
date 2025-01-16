#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	int total = 0, tmp = 0;
	while (n--) {
		int point;
		cin >> point;
		if (point == 1) tmp += point;
		else {
			total += tmp * (tmp + 1) / 2;
			tmp = 0;
		}
	}
	if (tmp != 0) total += tmp * (tmp + 1) / 2;
	cout << total;
}