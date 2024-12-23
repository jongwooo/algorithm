#include <iostream>
#define MAX 15
using namespace std;

int n, cnt = 0;
int col[MAX] = { 0, };

bool promising(int i) {
	int k = 1;
	while (k < i) {
		if (col[i] == col[k] || abs(col[i] - col[k]) == i - k) {
			return false;
		}
		k++;
	}
	return true;
}

void nQueens(int i) {
	if (promising(i)) {
		if (i == n) cnt++;
		else {
			for (int j = 1; j <= n; j++) {
				col[i + 1] = j;
				nQueens(i + 1);
			}
		}
	}
}

int main() {
	cin.tie(0)->sync_with_stdio(0);
	
	cin >> n;
	nQueens(0);
	cout << cnt;
}