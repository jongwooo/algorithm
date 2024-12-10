#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	string a, b;
	cin >> a >> b;

	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());

	if (a > b) {
		cout << a;
	}
	else {
		cout << b;
	}
}