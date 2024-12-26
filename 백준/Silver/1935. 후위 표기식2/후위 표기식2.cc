#include <iostream>
#include <string>
#include <stack>;
#define MAX 26
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	string exp;
	double nums[MAX];
	stack<double> s;
	cin >> n >> exp;
	for (int i = 0; i < n; i++) {
		cin >> nums[i];
	}
	for (char& c : exp) {
		if ('A' <= c && c <= 'Z') {
			s.push(nums[c - 'A']);
		}
		else {
			double n2 = s.top();
			s.pop();
			double n1 = s.top();
			s.pop();
			if (c == '+') {;
				s.push(n1 + n2);
			}
			else if (c == '-') {
				s.push(n1 - n2);
			}
			else if (c == '*') {
				s.push(n1 * n2);
			}
			else if (c == '/') {
				s.push(n1 / n2);
			}
		}
	}

	cout << fixed;
	cout.precision(2);
	cout << s.top();
}