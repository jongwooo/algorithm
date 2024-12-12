#include <iostream>
#include <algorithm>
using namespace std;

int num[1000];

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num[i];
	}
	sort(num, num + n);
	for (int i = 0; i < n; i++) {
		cout << num[i] << '\n';
	}
}