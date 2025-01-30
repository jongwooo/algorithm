#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	cin >> t;
	while (t--) {
		int points[5];
		for (int i = 0; i < 5; i++) {
			cin >> points[i];
		}
		sort(points, points + 5);
		if (4 <= points[3] - points[1]) cout << "KIN" << '\n';
		else cout << points[1] + points[2] + points[3] << '\n';
	}
}