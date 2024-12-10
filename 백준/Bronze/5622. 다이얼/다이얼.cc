#include <iostream>
#include <string>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	const string DIALS[8] = { "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ" };

	string s;
	int time = 0;
	
	cin >> s;

	for (char c : s) {
		for (int i = 0; i < 8; i++) {
			if (DIALS[i].find(c) != string::npos) {
				time += i + 3;
				break;
			}
		}
	}

	cout << time;
}