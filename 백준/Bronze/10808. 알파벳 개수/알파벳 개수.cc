#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	char s[101];
	cin >> s;
	int alphabets[26] = { 0, };
	for (int i = 0; s[i] != '\0'; i++) {
		alphabets[s[i] - 'a']++;
	}
	for (int i = 0; i < 26; i++) {
		cout << alphabets[i] << ' ';
	}
}