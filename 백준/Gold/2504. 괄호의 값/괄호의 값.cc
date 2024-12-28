#include <iostream>
#include <stack>
#define MAX 31
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	char s[MAX];
	cin >> s;
	stack<char> st;
	int res = 0, tmp = 1;
	for (int i = 0; s[i] != '\0'; i++) {
		if (s[i] == '(') {
			tmp *= 2;
			st.push(s[i]);
		}
		else if (s[i] == '[') {
			tmp *= 3;
			st.push(s[i]);
		}
		else if (s[i] == ')') {
			if (st.empty() || st.top() != '(') {
				res = 0;
				break;
			}
			else if (s[i - 1] == '(') {
				res += tmp;
			}
			tmp /= 2;
			st.pop();
		}
		else if (s[i] == ']') {
			if (st.empty() || st.top() != '[') {
				res = 0;
				break;
			}
			else if (s[i - 1] == '[') {
				res += tmp;
			}
			tmp /= 3;
			st.pop();
		}
	}
	if (!st.empty()) res = 0;
	cout << res;
}