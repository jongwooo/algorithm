#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	char s[101];
	cin >> s;
	for (int i = 0; s[i] != '\0'; i++) {
		cout << s[i];
		if ((i + 1) % 10 == 0) cout << '\n';
	}
}