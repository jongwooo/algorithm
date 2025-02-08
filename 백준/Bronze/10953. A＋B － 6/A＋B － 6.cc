#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	cin >> t;
	while (t--) {
		int a, b;
		char comma;
		cin >> a >> comma >> b;
		cout << a + b << '\n';
	}
}