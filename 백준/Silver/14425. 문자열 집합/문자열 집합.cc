#include <iostream>
#include <string>
#include <set>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, m;
	cin >> n >> m;
	set<string> s;
	string str;
	for (int i = 0; i < n; i++) {
		cin >> str;
		s.insert(str);
	}
	int cnt = 0;
	for (int i = 0; i < m; i++) {
		cin >> str;
		if (s.find(str) != s.end()) cnt++;
	}
	cout << cnt;
}