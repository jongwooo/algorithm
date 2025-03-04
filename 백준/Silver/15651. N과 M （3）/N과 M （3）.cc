#include <iostream>
#define MAX 8
using namespace std;

int n, m;
int arr[MAX];

void dfs(int depth) {
	if (depth == m) {
		for (int i = 0; i < m; i++) {
			cout << arr[i] << ' ';
		}
		cout << '\n';
		return;
	}
	for (int i = 1; i <= n; i++) {
		arr[depth] = i;
		dfs(depth + 1);
	}
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> n >> m;
	dfs(0);
}