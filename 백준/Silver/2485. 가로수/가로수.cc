#include <iostream>
#include <algorithm>
using namespace std;

int trees[100'000], gaps[100'000];

int gcd(int a, int b) {
	if (b == 0) return a;
	return gcd(b, a % b);
}


int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> trees[i];
	}
	sort(trees, trees + n);
	for (int i = 0; i < n - 1; i++) {
		gaps[i] = trees[i + 1] - trees[i];
	}
	int gapGcd = gaps[0];
	for (int i = 1; i < n - 1; i++) {
		gapGcd = gcd(gapGcd, gaps[i]);
	}
	int cnt = 0;
	for (int i = 0; i < n - 1; i++) {
		cnt += (gaps[i] / gapGcd) - 1;
	}
	cout << cnt;
}