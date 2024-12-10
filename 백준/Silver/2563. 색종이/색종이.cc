#include <iostream>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int matrix[100][100] = { 0 };
	int n, x, y;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> x >> y;
		for (int j = x; j < x + 10; j++) {
			for (int k = y; k < y + 10; k++) {
				if (matrix[j][k] == 0) matrix[j][k] = 1;
			}
		}
	}
	int area = 0;
	for (int i = 0; i < 100; i++) {
		for (int j = 0; j < 100; j++) {
			if (matrix[i][j]) area++;
		}
	}

	cout << area;
}