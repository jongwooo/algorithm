#include <iostream>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;

	cin >> n;

	int count = 1, temp = 1;
	while (n > temp) {
		temp += 6 * count;
		count++;
	}

	cout << count;
}