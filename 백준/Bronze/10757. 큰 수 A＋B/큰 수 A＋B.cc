#include <iostream>
#include <string>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	string a, b, res;
	cin >> a >> b;
	int car = 0;
	int aSize = a.size();
	int bSize = b.size();
	while (aSize > 0 || bSize > 0) {
		int aDigit = 0;
		if (aSize > 0) aDigit = a[--aSize] - '0';
		int bDigit = 0;
		if (bSize > 0) bDigit = b[--bSize] - '0';
		int cur = aDigit + bDigit + car;
		car = cur / 10;
		cur %= 10;
		res += cur + '0';
	}
	if (car > 0) res += car + '0';
	for (int i = res.size() - 1; i >= 0; i--) {
		cout << res[i];
	}
}