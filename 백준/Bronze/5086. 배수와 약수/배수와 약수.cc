#include <iostream>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int a, b;
	while (true) {
		cin >> a >> b;
		if (a == 0 && b == 0) break;
		if (a % b == 0) {
			cout << "multiple";
		}
		else if (b % a == 0) {
			cout << "factor";
		}
		else {
			cout << "neither";
		}
		cout << '\n';
	}
}