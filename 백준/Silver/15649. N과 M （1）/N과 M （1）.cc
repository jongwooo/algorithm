#include <iostream>
#define MAX 9
using namespace std;

int n, m;
int arr[MAX];
bool visited[MAX];

void permutations(int depth) {
	if (depth == m) {
		for (int i = 0; i < m; i++) {
			cout << arr[i] << ' ';
		}
		cout << '\n';
		return;
	}
	for (int i = 1; i <= n; i++) {
		if (!visited[i]) {
			visited[i] = true;
			arr[depth] = i;
			permutations(depth + 1);
			visited[i] = false;
		}
	}
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> n >> m;
	permutations(0);
}