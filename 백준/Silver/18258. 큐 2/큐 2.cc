#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, x;
	cin >> n;
	string cmd;
	queue<int> q;
	while (n--) {
		cin >> cmd;
		if (cmd == "push") {
			cin >> x;
			q.push(x);
			continue;
		}
		else if (cmd == "pop") {
			if (q.empty()) cout << -1;
			else {
				cout << q.front();
				q.pop();
			}
		}
		else if (cmd == "size") {
			cout << q.size();
		}
		else if (cmd == "empty") {
			cout << (q.empty() ? 1 : 0);
		}
		else if (cmd == "front") {
			if (q.empty()) cout << -1;
			else cout << q.front();
		}
		else if (cmd == "back") {
			if (q.empty()) cout << -1;
			else cout << q.back();
		}
		cout << '\n';
	}
}