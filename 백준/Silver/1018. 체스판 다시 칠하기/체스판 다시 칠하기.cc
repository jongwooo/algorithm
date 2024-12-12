#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

const char WHITE = 'W';

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, m;
	string board[50];
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> board[i];
	}
	int minCnt = 64;
	for (int i = 0; i <= n - 8; i++) {
		for (int j = 0; j <= m - 8; j++) {
			int w = 0, b = 0;
			for (int x = i; x < i + 8; x++) {
				for (int y = j; y < j + 8; y++) {
					if ((x + y) % 2 == 0) {
						if (board[x][y] != WHITE) w++;
						else b++;
					}
					else {
						if (board[x][y] != WHITE) b++;
						else w++;
					}
				}
			}
			minCnt = min({ minCnt , w, b });
		}
	}
	cout << minCnt;
}