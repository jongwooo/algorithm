#include <iostream>
#include <algorithm>
using namespace std;

int x, y, w, h;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> x >> y >> w >> h;
	cout << min({ x, y, w - x, h - y });
}