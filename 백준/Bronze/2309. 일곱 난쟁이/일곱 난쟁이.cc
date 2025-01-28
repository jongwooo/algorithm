#include <iostream>
#include <algorithm>
using namespace std;

void dfs(int depth, int next);

int nineDwarfs[9];
int sevenDwarfs[7] = { 0, };

int main() {
	cin.tie(0)->sync_with_stdio(0);

	for (int i = 0; i < 9; i++) {
		cin >> nineDwarfs[i];
	}
	sort(nineDwarfs, nineDwarfs + 9);
	dfs(0, 0);
}

void dfs(int depth, int next) {
	if (depth == 7) {
		int sum = 0;
		for (int dwarf : sevenDwarfs) {
			sum += dwarf;
		}
		if (sum == 100) {
			for (int dwarf : sevenDwarfs) {
				cout << dwarf << '\n';
			}
			exit(0);
		}
		return;
	}
	for (int i = next; i < 9; i++) {
		sevenDwarfs[depth] = nineDwarfs[i];
		dfs(depth + 1, i + 1);
	}
}