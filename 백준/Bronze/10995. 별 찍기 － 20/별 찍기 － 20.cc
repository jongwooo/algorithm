#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (i % 2 == 0) cout << '*' << ' ';
			else cout << ' ' << '*';
		}
		cout << '\n';
	}
}