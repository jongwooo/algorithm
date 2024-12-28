#include <iostream>
#define MAX 51
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	
	char s[MAX];
	cin >> s;
	int height = 0;
	char cur = ' ';
	for (int i = 0; s[i] != '\0'; i++) {
		if (cur == s[i]) height += 5;
		else {
			cur = s[i];
			height += 10;
		}
	}
	cout << height;
}