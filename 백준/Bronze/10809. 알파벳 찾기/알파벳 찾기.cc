#include <iostream>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	string s;
	int indexes[26];
	fill_n(indexes, 26, -1);

	cin >> s;
	int v;
	for (int i = 0; i < s.length(); i++) {
		v = s[i] - 'a';
		if (indexes[v] != -1) {
			continue;
		}
		indexes[v] = i;
	}

	for (int i : indexes) {
		cout << i << " ";
	}
}