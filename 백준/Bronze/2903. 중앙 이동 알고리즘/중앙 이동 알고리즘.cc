#include <iostream>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	
	int n;

	cin >> n;

	int sideDots = 2;
	for (int i = 0; i < n; i++) {
		sideDots *= 2;
		sideDots--;
	}

	cout << sideDots * sideDots;
}