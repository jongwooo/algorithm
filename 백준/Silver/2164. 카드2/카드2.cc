#include <iostream>
#include <queue>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	if (n == 1) {
		cout << 1;
		return 0;
	}
	queue<int> q;
	for (int i = 1; i <= n; i++) {
		q.push(i);
	}
	while (true) {
		q.pop();
		if (q.size() == 1) break;
		q.push(q.front());
		q.pop();
	}
	cout << q.front();
}