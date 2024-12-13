#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string word[20000];

bool compare(string s1, string s2) {
	if (s1.length() == s2.length()) return s1 < s2;
	return s1.length() < s2.length();
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> word[i];
	}
	sort(word, word + n, compare);
	for (int i = 0; i < n; i++) {
		if (i > 0 && word[i] == word[i - 1]) continue;
		cout << word[i] << '\n';
	}
}