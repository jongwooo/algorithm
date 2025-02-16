#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	char s[101];
	cin >> s;
	int cnt = 1;
	for (int i = 0; s[i] != '\0'; i++) {
		if (s[i] == ',') cnt++;
	}
	cout << cnt;
}