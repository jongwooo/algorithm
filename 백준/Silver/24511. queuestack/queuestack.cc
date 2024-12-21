#include <iostream>
#include <deque>
using namespace std;

int n, m;
int a[100'000], b[100'000], c[100'000];
deque<int> dq;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	for (int i = 0; i < n; i++) {
		cin >> b[i];
	}
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> c[i];
	}
	for (int i = 0; i < n; i++) {
		if (a[i] == 0) dq.push_front(b[i]);
	}
	for (int i = 0; i < m; i++) {
		dq.push_back(c[i]);
		cout << dq.front() << ' ';
		dq.pop_front();
	}
}