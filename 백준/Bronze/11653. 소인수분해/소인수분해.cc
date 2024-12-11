#include <iostream>
using namespace std;

int n;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> n;
	if (n == 1) return 0;
	int i = 2;
	while (n > 1) {
		if (n % i == 0) {
			cout << i << '\n';
			n /= i;
		}
		else {
			i++;
		}
	}
}