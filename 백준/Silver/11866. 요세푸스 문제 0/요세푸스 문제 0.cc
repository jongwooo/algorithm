#include <iostream>
#include <queue>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, k;
	cin >> n >> k;
	queue<int> q, res;
	for (int i = 1; i <= n; i++) {
		q.push(i);
	}
	while (!q.empty()) {
		for (int i = 0; i < k - 1; i++) {
			q.push(q.front());
			q.pop();
		}
		res.push(q.front());
		q.pop();
	}
	cout << '<';
	while (true) {
		cout << res.front();
		res.pop();
		if (res.empty()) break;
		else cout << ", ";
	}
	cout << '>';
}