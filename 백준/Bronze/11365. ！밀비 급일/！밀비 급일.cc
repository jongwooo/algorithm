#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	string s;
	while (true) {
		getline(cin, s);
		if (s == "END") break;
		reverse(s.begin(), s.end());
		cout << s << '\n';
	}
}