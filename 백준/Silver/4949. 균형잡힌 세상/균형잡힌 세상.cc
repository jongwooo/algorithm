#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	string s;
	while (true) {
		getline(cin, s);
		if (s == ".") break;
		stack<char> st;
		for (char& c : s) {
			if (c == '(' || c == '[') {
				st.push(c);
			}
			else if (c == ')') {
				if (!st.empty() && st.top() == '(') {
					st.pop();
				}
				else {
					st.push(c);
					break;
				}
			}
			else if (c == ']') {
				if (!st.empty() && st.top() == '[') {
					st.pop();
				}
				else {
					st.push(c);
					break;
				}
			}
		}
		if (st.empty()) cout << "yes" << '\n';
		else cout << "no" << '\n';
	}
}