#include <iostream>
#include <deque>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, cmd, x;
	cin >> n;
	deque<int> q;
	while (n--) {
		cin >> cmd;
		if (cmd == 1) {
			cin >> x;
			q.push_front(x);
			continue;
		}
		else if (cmd == 2) {
			cin >> x;
			q.push_back(x);
			continue;
		}
		else if (cmd == 3) {
			if (q.empty()) cout << -1;
			else {
				cout << q.front();
				q.pop_front();
			}
		}
		else if (cmd == 4) {
			if (q.empty()) cout << -1;
			else {
				cout << q.back();
				q.pop_back();
			}
		}
		else if (cmd == 5) {
			cout << q.size();
		}
		else if (cmd == 6) {
			cout << (q.empty() ? 1 : 0);
		}
		else if (cmd == 7) {
			if (q.empty()) cout << -1;
			else cout << q.front();
		}
		else if (cmd == 8) {
			if (q.empty()) cout << -1;
			else cout << q.back();
		}
		cout << '\n';
	}
}