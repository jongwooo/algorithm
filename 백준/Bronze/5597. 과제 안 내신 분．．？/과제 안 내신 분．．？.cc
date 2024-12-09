#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	bool submit[31] = { 0, };
	int num;
	for (int i = 0; i < 28; i++) {
		cin >> num;
		submit[num] = 1;
	}
	for (int i = 1; i <= 30; i++) {
		if (!submit[i]) cout << i << '\n';
	}
}