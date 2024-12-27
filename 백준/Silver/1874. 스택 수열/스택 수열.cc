#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	stack<int> s;
	vector<char> op;
	int cnt = 1;
	while (n--) {
		int x;
		cin >> x;
		while (cnt <= x) {
			s.push(cnt);
			op.push_back('+');
			cnt++;
		}
		if (s.top() == x) {
			s.pop();
			op.push_back('-');
		}
		else {
			cout << "NO";
			return 0;
		}
	}
	for (char& c : op) {
		cout << c << '\n';
	}
}