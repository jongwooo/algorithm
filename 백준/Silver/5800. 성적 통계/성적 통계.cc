#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int k;
	cin >> k;
	for (int i = 1; i <= k; i++) {
		int n;
		cin >> n;
		int scores[51];
		for (int j = 0; j < n; j++) {
			cin >> scores[j];
		}
		sort(scores, scores + n);
		int gap = 0;
		for (int j = 0; j < n - 1; j++) {
			int v = scores[j + 1] - scores[j];
			if (gap < v) gap = v;
		}
		cout << "Class " << i << '\n';
		cout << "Max " << scores[n - 1] << ", Min " << scores[0] << ", Largest gap " << gap << '\n';
	}
}