#include <iostream>
#include <string>
#include <set>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	string s;
	cin >> s;
	set<string> sub;
	for (int i = 0; i < s.length(); i++) {
		string temp;
		for (int j = i; j < s.length(); j++) {
			temp += s[j];
			sub.emplace(temp);
		}
	}
	cout << sub.size();
}