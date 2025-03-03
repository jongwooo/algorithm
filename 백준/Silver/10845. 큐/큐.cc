#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	string cmd;
	int x;
	queue<int> q;
	while (n--) {
		cin >> cmd;
		if (cmd == "push") {
			cin >> x;
			q.push(x);
		}
		else if (cmd == "pop") {
			if (q.empty()) cout << -1 << '\n';
			else {
				cout << q.front() << '\n';
				q.pop();
			}
		}
		else if (cmd == "size") {
			cout << q.size() << '\n';
		}
		else if (cmd == "empty") {
			cout << q.empty() << '\n';
		}
		else if (cmd == "front") {
			if (q.empty()) cout << -1 << '\n';
			else cout << q.front() << '\n';
		}
		else if (cmd == "back") {
			if (q.empty()) cout << -1 << '\n';
			else cout << q.back() << '\n';
		}
	}
}