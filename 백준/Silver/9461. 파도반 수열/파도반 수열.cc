#include <iostream>
#define MAX 101
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	long long p[MAX] = { 0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9 };
	for (int i = 11; i < MAX; i++) {
		p[i] = p[i - 1] + p[i - 5];
	}
	int t, n;
	cin >> t;
	while (t--) {
		cin >> n;
		cout << p[n] << '\n';
	}
}