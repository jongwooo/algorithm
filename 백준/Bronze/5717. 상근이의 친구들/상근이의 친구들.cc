#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int m, f;
	while (true) {
		cin >> m >> f;
		if (m == 0 && f == 0) break;
		cout << m + f << '\n';
	}
}