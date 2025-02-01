#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int k;
	cin >> k;
	while (k--) {
		int p, m;
		cin >> p >> m;
		int seats[501] = { 0, };
		int cnt = 0;
		for (int i = 0; i < p; i++) {
			int s;
			cin >> s;
			if (seats[s] == 0) seats[s] = 1;
			else cnt++;
		}
		cout << cnt << '\n';
	}
}