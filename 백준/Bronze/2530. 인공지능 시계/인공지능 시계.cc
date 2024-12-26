#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int a, b, c, d;
	cin >> a >> b >> c >> d;
	int h = d / 3'600;
	int m = (d % 3'600) / 60;
	int s = d % 60;
	c += s;
	if (c >= 60) {
		b += c / 60;
		c %= 60;
	}
	b += m;
	if (b >= 60) {
		a += b / 60;
		b %= 60;
	}
	a += h;
	if (a >= 24) {
		a %= 24;
	}
	cout << a << ' ' << b << ' ' << c;
}