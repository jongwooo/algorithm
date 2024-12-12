#include <iostream>
using namespace std;

int n, m, cards[100];
int maxSum = 0;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> cards[i];
	}
	for (int i = 0; i < n - 2; i++) {
		for (int j = i + 1; j < n - 1; j++) {
			for (int k = j + 1; k < n; k++) {
				int sum = cards[i] + cards[j] + cards[k];
				if (m < sum) continue;
				if (maxSum < sum) maxSum = sum;
			}
		}
	}
	cout << maxSum;
}