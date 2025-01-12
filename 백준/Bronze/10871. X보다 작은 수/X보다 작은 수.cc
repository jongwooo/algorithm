#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, x;
	cin >> n >> x;
	while (n--) {
		int num;
		cin >> num;
		if (num < x) cout << num << ' ';
	}
}