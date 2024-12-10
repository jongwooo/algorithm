#include <iostream>
#include <string>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	
	const string alphabets[8] = { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" };
	string s;
	int index;

	cin >> s;
	for (string alphabet : alphabets) {
		while (true) {
			index = s.find(alphabet);
			if (index == string::npos) break;
			s.replace(index, alphabet.length(), "*");
		}
	}

	cout << s.length();
}