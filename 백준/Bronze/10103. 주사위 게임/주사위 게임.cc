#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	
	int n;
	cin >> n;
	int c = 100, s = 100;
	while (n--) {
		int d1, d2;
		cin >> d1 >> d2;
		if (d1 == d2) continue;
		else if (d1 > d2) s -= d1;
		else c -= d2;
	}
	cout << c << '\n' << s;
}