#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	cin >> t;
	while (t--) {
		stack<char> st;
		string s;
		cin >> s;
		for (int i = 0; i < s.length(); i++) {
			st.push(s[i]);
		}
		int cnt = 0;
		while (!st.empty()) {
			if (st.top() == ')') cnt++;
			else cnt--;
			if (cnt < 0) break;
			st.pop();
		}
		if (cnt == 0) cout << "YES";
		else cout << "NO";
		cout << '\n';
	}
}