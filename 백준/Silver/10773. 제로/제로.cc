#include <iostream>
#include <stack>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int k;
	cin >> k;
	stack<int> st;
	int n;
	while (k--) {
		cin >> n;
		if (n == 0) st.pop();
		else st.push(n);
	}
	int sum = 0;
	while (!st.empty()) {
		sum += st.top();
		st.pop();
	}
	cout << sum;
}