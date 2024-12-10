#include <iostream>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int x;
	cin >> x;
	int row = 1;
	while (x > row) {
		x -= row;
		row++;
	}
	int a = x;
	int b = row - x + 1;
	if (row % 2 == 0) cout << a << "/" << b;
	else cout << b << "/" << a;
}