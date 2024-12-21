#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int a;
	int b[50];
	cin >> a;
	for (int i = 0; i < a; i++) {
		cin >> b[i];
	}
	sort(b, b + a);
	if (a % 2 == 0) cout << b[0] * b[a - 1];
	else cout << b[(a - 1) / 2] * b[(a - 1) / 2];
}