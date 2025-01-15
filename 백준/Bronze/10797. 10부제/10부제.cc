#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	int cnt = 0;
	for (int i = 0; i < 5; i++) {
		int num;
		cin >> num;
		if (n == num) cnt++;
	}
	cout << cnt;
}