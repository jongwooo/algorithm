#include <iostream>
#define MAX 20
using namespace std;

int n, minDiff = 100;
int s[MAX][MAX];
bool visited[MAX];

void dfs(int depth, int idx) {
	if (depth == n / 2) {
		int start = 0, link = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (visited[i] && visited[j]) start += s[i][j];
				else if (!visited[i] && !visited[j]) link += s[i][j];
			}
		}
		int diff = abs(start - link);
		if (diff < minDiff) minDiff = diff;
		return;
	}
	for (int i = idx; i < n; i++) {
		visited[i] = true;
		dfs(depth + 1, i + 1);
		visited[i] = false;
	}
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> s[i][j];
		}
	}
	dfs(0, 0);
	cout << minDiff;
}