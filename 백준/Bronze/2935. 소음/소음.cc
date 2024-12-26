#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	string a, b;
	char op;
	cin >> a >> op >> b;
	int aSize = a.size();
	int bSize = b.size();
	if (op == '*') {
		cout << 1;
		for (int i = 0; i < aSize + bSize - 2; i++) {
			cout << 0;
		}
	}
	else if (op == '+') {
		if (aSize == bSize) {
			cout << 2;
			for (int i = 0; i < aSize - 1; i++) {
				cout << 0;
			}
		}
		else {
			int maxDigit = max(aSize, bSize);
			int minDigit = min(aSize, bSize);
			for (int i = maxDigit; i > 0; i--) {
				if (i == maxDigit || i == minDigit) cout << 1;
				else cout << 0;
			}
		}
	}
}