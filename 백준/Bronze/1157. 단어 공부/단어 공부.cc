#include <iostream>
#include <string>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	
	int alphabets[26] = { 0, };
	string s;

	cin >> s;

	for (char c : s) {
		if (c < 97) alphabets[c - 65]++;
		else alphabets[c - 97]++;
		
	}
	int maxCount = 0, maxIndex = 0;
	for (int i = 0; i < 26; i++) {
		if (maxCount < alphabets[i]) {
			maxCount = alphabets[i];
			maxIndex = i;
		}
	}
	int count = 0;
	for (int a : alphabets) {
		if (maxCount == a) count++;
	}
	if (count > 1) cout << "?";
	else cout << (char)(maxIndex + 65);
}