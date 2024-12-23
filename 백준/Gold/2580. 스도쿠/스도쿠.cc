#include <iostream>
using namespace std;

typedef pair<int, int> pii;

int grid[9][9];
int idx = 0;
pii pos[81];

bool checkRow(int r, int n) {
	for (int i = 0; i < 9; i++) {
		if (n == grid[r][i]) return false;
	}
	return true;
}

bool checkCol(int c, int n) {
	for (int i = 0; i < 9; i++) {
		if (n == grid[i][c]) return false;
	}
	return true;
}

bool checkSquare(int r, int c, int n) {
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (n == grid[r - r % 3 + i][c - c % 3 + j]) return false;
		}
	}
	return true;
}

void sudoku(int n) {
	if (n == idx) {
		for (int r = 0; r < 9; r++) {
			for (int c = 0; c < 9; c++) {
				cout << grid[r][c] << ' ';
			}
			cout << '\n';
		}
		exit(0);
	}
	for (int i = 1; i <= 9; i++) {
		pii cur = pos[n];
		int r = cur.first;
		int c = cur.second;
		if (checkRow(r, i) && checkCol(c, i) && checkSquare(r, c, i)) {
			grid[r][c] = i;
			sudoku(n + 1);
			grid[r][c] = 0;
		}
	}
}

int main() {
	cin.tie(0)->sync_with_stdio(0);
	
	for (int r = 0; r < 9; r++) {
		for (int c = 0; c < 9; c++) {
			cin >> grid[r][c];
			if (grid[r][c] == 0) pos[idx++] = make_pair(r, c);
		}
	}
	sudoku(0);
}