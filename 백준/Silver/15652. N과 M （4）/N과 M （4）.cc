#include <iostream>
#define MAX 9
using namespace std;

int n, m;
int arr[MAX];

void dfs(int depth, int index) {
	if (depth == m) {
		for (int i = 0; i < m; i++) {
			cout << arr[i] << ' ';
		}
		cout << '\n';
		return;
	}
	for (int i = index; i <= n; i++) {
		arr[depth] = i;
		dfs(depth + 1, i);
	}
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> n >> m;
	dfs(0, 1);
}