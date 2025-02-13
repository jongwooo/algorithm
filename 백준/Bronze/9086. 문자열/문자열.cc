#include <iostream>
#include <string>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	string s;

	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> s;
		cout << s[0] << s[s.length() - 1] << '\n';
	}
}