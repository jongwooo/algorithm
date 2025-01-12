#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int sum = 0;
	for (int i = 0; i < 5; i++) {
		int n;
		cin >> n;
		sum += n * n;
	}
	cout << sum % 10;
}