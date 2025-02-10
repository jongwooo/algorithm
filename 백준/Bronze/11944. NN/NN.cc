#include <iostream>
#include <string>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, m;
	cin >> n >> m;
	string s = "";
	for (int i = 0; i < n; i++) {
		s += to_string(n);
		if (s.size() >= m) {
			s = s.substr(0, m);
			break;
		}
	}
	cout << s;
}