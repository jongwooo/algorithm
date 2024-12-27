#include <iostream>
#include <queue>
using namespace std;

typedef pair<int, int> pii;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t, n, m, v;
	cin >> t;
	while (t--) {
		cin >> n >> m;
		queue<pii> q;
		priority_queue<int> pq;
		for (int i = 0; i < n; i++) {
			cin >> v;
			q.push(make_pair(i, v));
			pq.push(v);
		}
		int cnt = 0;
		while (!q.empty()) {
			int idx = q.front().first;
			int val = q.front().second;
			q.pop();
			if (pq.top() == val) {
				pq.pop();
				cnt++;
				if (idx == m) {
					cout << cnt << '\n';
					break;
				}
			}
			else q.push(make_pair(idx, val));
		}
	}
}