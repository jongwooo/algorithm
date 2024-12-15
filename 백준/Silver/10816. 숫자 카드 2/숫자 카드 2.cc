#include <iostream>
#include <algorithm>
using namespace std;

int n, m, num;
int cards[500'000];

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
		cout << upper_bound(cards, cards + n, num) - lower_bound(cards, cards + n, num) << ' ';
	}
}