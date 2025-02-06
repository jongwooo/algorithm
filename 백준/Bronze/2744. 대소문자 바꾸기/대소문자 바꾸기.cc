#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	char s[101];
	cin >> s;
	for (int i = 0; s[i] != '\0'; i++) {
		if (65 <= s[i] && s[i] <= 90) s[i] += 32;
		else s[i] -= 32;
		cout << s[i];
	}
}