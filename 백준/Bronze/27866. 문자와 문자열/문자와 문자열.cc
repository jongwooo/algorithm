#include <iostream>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	string s;
	int i;

	cin >> s >> i;

	cout << s[i - 1];
}