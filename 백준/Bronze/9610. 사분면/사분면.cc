#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	int q[5] = { 0, };
	while (n--) {
		int x, y;
		cin >> x >> y;
		if (x > 0 && y > 0) q[1]++;
		else if (x < 0 && 0 < y) q[2]++;
		else if (x < 0 && y < 0) q[3]++;
		else if (y < 0 && 0 < x) q[4]++;
		else q[0]++;
	}
	for (int i = 1; i <= 4; i++) {
		cout << "Q" << i << ": " << q[i] << '\n';
	}
	cout << "AXIS: " << q[0];
 }