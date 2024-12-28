#include <iostream>
#include <string>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	
	string s;
	cin >> s;
	int height = 0;
	char cur = ' ';
	for (char& c : s) {
		if (cur == c) height += 5;
		else {
			cur = c;
			height += 10;
		}
	}
	cout << height;
}