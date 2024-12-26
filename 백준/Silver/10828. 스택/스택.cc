#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, x;
	string cmd;
	stack<int> s;
	cin >> n;
	while (n--) {
		cin >> cmd;
		if (cmd == "push") {
			cin >> x;
			s.push(x);
			continue;
		}
		else if (cmd == "pop") {
			if (s.empty()) cout << -1;
			else {
				cout << s.top();
				s.pop();
			}
		}
		else if (cmd == "size") {
			cout << s.size();
		}
		else if (cmd == "empty") {
			cout << s.empty() ? 1 : 0;
		}
		else if (cmd == "top") {
			if (s.empty()) cout << -1;
			else cout << s.top();
		}
		cout << '\n';
	}
}