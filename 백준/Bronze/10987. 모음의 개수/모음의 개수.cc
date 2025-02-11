#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	char s[101];
	cin >> s;
	int cnt = 0;
	for (int i = 0; s[i] != '\0'; i++) {
		if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') cnt++;
	}
	cout << cnt;
}