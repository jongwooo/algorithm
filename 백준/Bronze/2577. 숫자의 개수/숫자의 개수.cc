#include <iostream>
#include <string>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int cnt[10] = {};
	int a, b, c;
	cin >> a >> b >> c;
	string s = to_string(a * b * c);
	for (char c : s) {
		cnt[c - '0']++;
	}
	for (int v : cnt) {
		cout << v << '\n';
	}
}