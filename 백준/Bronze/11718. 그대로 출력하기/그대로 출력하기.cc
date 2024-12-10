#include <iostream>
#include <string>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	string s;

	while (true) {
		getline(cin, s);
		if (s == "") break;
		cout << s << '\n';
	}
}