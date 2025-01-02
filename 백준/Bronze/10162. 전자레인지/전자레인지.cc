#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	cin >> t;
	int a = t / 300;
	t %= 300;
	int b = t / 60;
	t %= 60;
	int c = t / 10;
	t %= 10;
	if (t != 0) cout << -1;
	else cout << a << ' ' << b << ' ' << c;
}