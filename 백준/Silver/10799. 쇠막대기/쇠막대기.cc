#include <iostream>
#include <stack>
#define MAX 100'001
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	
	char s[MAX];
	cin >> s;
	stack<char> st;
	int cnt = 0;
	for (int i = 0; s[i] != '\0'; i++) {
		if (s[i] == '(') st.push(s[i]);
		else if (s[i - 1] == '(') {
			st.pop();
			cnt += st.size();
		}
		else {
			st.pop();
			cnt++;
		}
	}
	cout << cnt;
}