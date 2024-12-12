#include <iostream>
using namespace std;

int a1, a0, c, n0;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> a1 >> a0 >> c >> n0;
	if (a1 * n0 + a0 <= c * n0 && a1 <= c) cout << 1;
	else cout << 0;
}