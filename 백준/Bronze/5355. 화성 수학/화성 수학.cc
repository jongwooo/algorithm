#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	double n;
	char c;
	cin >> t;
	while (t--) {
		cin >> n;
		while (true) {
			cin.get(c);
			if (c == '\n') break;
			else if (c == '@') n *= 3;
			else if (c == '%') n += 5;
			else if (c == '#') n -= 7;
		}
		cout << fixed;
		cout.precision(2);
		cout << n << '\n';
	}
}