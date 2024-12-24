#include <iostream>
#include <climits>
#define MAX 11
using namespace std;

int n;
int a[MAX];
int op[4];
int maxNum = INT_MIN;
int minNum = INT_MAX;

void dfs(int i, int num) {
	if (i == n) {
		if (maxNum < num) maxNum = num;
		if (num < minNum) minNum = num;
	}
	if (op[0] > 0) {
		op[0]--;
		dfs(i + 1, num + a[i]);

		op[0]++;
	}
	if (op[1] > 0) {
		op[1]--;
		dfs(i + 1, num - a[i]);
		op[1]++;
	}
	if (op[2] > 0) {
		op[2]--;
		dfs(i + 1, num * a[i]);
		op[2]++;
	}
	if (op[3] > 0) {
		op[3]--;
		dfs(i + 1, num / a[i]);
		op[3]++;
	}
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	for (int i = 0; i < 4; i++) {
		cin >> op[i];
	}
	dfs(1, a[0]);
	cout << maxNum << '\n' << minNum;
}