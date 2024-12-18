#include <iostream>
#include <stack>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	stack<int> st;
	int num, idx = 1;
	for (int i = 0; i < n; i++) {
		cin >> num;
		if (idx == num) idx++;
		else st.push(num);
		while (!st.empty() && st.top() == idx) {
			st.pop();
			idx++;
		}
	}
	cout << (st.empty() ? "Nice" : "Sad");
}