#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	cin >> t;
	while (t--) {
		int yonsei = 0, korea = 0;
		for (int i = 0; i < 9; i++) {
			int y, k;
			cin >> y >> k;
			yonsei += y;
			korea += k;
		}
		if (yonsei < korea) cout << "Korea" << '\n';
		else if (yonsei > korea) cout << "Yonsei" << '\n';
		else cout << "Draw" << '\n';
	}
}