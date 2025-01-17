#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int max = 0, cur = 0;
	for (int i = 0; i < 4; i++) {
		int off, on;
		cin >> off >> on;
		cur -= off;
		cur += on;
		if (max < cur) max = cur;
	}
	cout << max;
}