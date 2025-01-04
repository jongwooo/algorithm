#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int sum, price;
	cin >> sum;
	for (int i = 0; i < 9; i++) {
		cin >> price;
		sum -= price;
	}
	cout << sum;
}