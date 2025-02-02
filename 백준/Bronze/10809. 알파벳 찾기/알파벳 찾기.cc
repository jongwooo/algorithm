#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	char s[101];
	cin >> s;
	int idx[26];
	fill_n(idx, 26, -1);
	for (int i = 0; s[i] != '\0'; i++) {
		if (idx[s[i] - 'a'] == -1) idx[s[i] - 'a'] = i;
	}
	for (int i = 0; i < 26; i++) {
		cout << idx[i] << ' ';
	}
}