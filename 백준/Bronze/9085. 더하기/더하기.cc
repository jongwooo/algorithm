#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		int sum = 0;
		while (n--) {
			int num;
			cin >> num;
			sum += num;
		}
		cout << sum << '\n';
	}
}
