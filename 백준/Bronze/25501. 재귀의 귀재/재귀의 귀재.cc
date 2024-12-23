#include <iostream>
#include <cstring>
using namespace std;

int cnt = 0;

int recursion(const char *s, int l, int r) {
	cnt++;
	if (l >= r) return 1;
	else if (s[l] != s[r]) return 0;
	return recursion(s, l + 1, r - 1);
}

int isPalindrome(const char *s) {
	return recursion(s, 0, strlen(s) - 1);
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int t;
	char s[1'001];
	cin >> t;
	while (t--) {
		cnt = 0;
		cin >> s;
		cout << isPalindrome(s);
		cout << ' ' << cnt << '\n';
	}
}