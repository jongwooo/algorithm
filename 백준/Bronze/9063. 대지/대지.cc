#include <iostream>
using namespace std;

int n, x, y;
int minX = 10001, maxX = -10001;
int minY = 10001, maxY = -10001;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	
	cin >> n;
	if (n == 1) {
		cout << 0;
		return 0;
	}
	for (int i = 0; i < n; i++) {
		cin >> x >> y;
		if (maxX < x) maxX = x;
		if (x < minX) minX = x;
		if (maxY < y) maxY = y;
		if (y < minY) minY = y;
	}
	cout << (maxX - minX) * (maxY - minY);
	return 0;
}