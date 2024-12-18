#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	int cnt = 0;
	for (int i = 1; i * i <= n; i++) {
		cnt++;
	}
	cout << cnt;
}