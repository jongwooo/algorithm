#include <iostream>
#include <stack>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	stack<int> st;
	while (n--) {
		int cmd, x;
		cin >> cmd;
		if (cmd == 1) {
			cin >> x;
			st.push(x);
			continue;
		}
		else if (cmd == 2) {
			if (st.empty()) cout << -1;
			else {
				cout << st.top();
				st.pop();
			}
		}
		else if (cmd == 3) {
			cout << st.size();
		}
		else if (cmd == 4) {
			if (st.empty()) cout << 1;
			else cout << 0;
		}
		else if (cmd == 5) {
			if (st.empty()) cout << -1;
			else cout << st.top();
		}
		cout << '\n';
	}
}