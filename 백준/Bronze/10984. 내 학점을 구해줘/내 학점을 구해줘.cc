#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cout << fixed;
	cout.precision(1);

	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		int s = 0;
		double p = 0.0;
		while (n--) {
			int c;
			double g;
			cin >> c >> g;
			s += c;
			p += g * c;
		}
		cout << s << ' ' << p / s << '\n';
	}
}