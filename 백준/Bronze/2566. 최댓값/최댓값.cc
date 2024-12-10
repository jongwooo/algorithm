#include <iostream>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int num;
	int max = 0, x = 0, y = 0;

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> num;
			if (max < num) {
				max = num;
				x = i;
				y = j;
			}
		}
	}

	cout << max << '\n' << x + 1 << ' ' << y + 1;
}