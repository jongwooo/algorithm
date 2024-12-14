#include <iostream>
#include <algorithm>
using namespace std;

int n, m, num;
int cards[500'000];

int binary(int x) {
	int start = 0, end = n - 1;
	while (start <= end) {
		int mid = (start + end) / 2;
		if (cards[mid] == x) return 1;
		else if (cards[mid] < x) start = mid + 1;
		else end = mid - 1;
	}
	return 0;
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> cards[i];
	}
	sort(cards, cards + n);
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> num;
		cout << binary(num) << ' ';
	}
}