#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	while (n--) {
		int r, e, c;
		cin >> r >> e >> c;
		if (r < e - c) cout << "advertise" << '\n';
		else if (r == e - c) cout << "does not matter" << '\n';
		else cout << "do not advertise" << '\n';
	}
}