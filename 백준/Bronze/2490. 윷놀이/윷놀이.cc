#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	for (int i = 0; i < 3; i++) {
		int cnt = 0;
		for (int j = 0; j < 4; j++) {
			int yut;
			cin >> yut;
			cnt += yut;
		}
		if (cnt == 1) cout << 'C' << '\n';
		else if (cnt == 2) cout << 'B' << '\n';
		else if (cnt == 3) cout << 'A' << '\n';
		else if (cnt == 4) cout << 'E' << '\n';
		else cout << 'D' << '\n';
	}
}