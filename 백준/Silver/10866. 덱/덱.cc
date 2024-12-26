#include <iostream>
#include <string>
#include <deque>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, x;
	string cmd;
	deque<int> dq;
	cin >> n;
	while (n--) {
		cin >> cmd;
		if (cmd == "push_front") {
			cin >> x;
			dq.push_front(x);
			continue;
		}
		else if (cmd == "push_back") {
			cin >> x;
			dq.push_back(x);
			continue;
		}
		else if (cmd == "pop_front") {
			if (dq.empty()) cout << -1;
			else {
				cout << dq.front();
				dq.pop_front();
			}
		}
		else if (cmd == "pop_back") {
			if (dq.empty()) cout << -1;
			else {
				cout << dq.back();
				dq.pop_back();
			}
		}
		else if (cmd == "size") {
			cout << dq.size();
		}
		else if (cmd == "empty") {
			cout << dq.empty() ? 1 : 0;
		}
		else if (cmd == "front") {
			if (dq.empty()) cout << -1;
			else cout << dq.front();
		}
		else if (cmd == "back") {
			if (dq.empty()) cout << -1;
			else cout << dq.back();
		}
		cout << '\n';
	}
}