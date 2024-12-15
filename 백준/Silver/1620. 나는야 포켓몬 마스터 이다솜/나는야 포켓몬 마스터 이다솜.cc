#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, m;
	cin >> n >> m;
	map<int, string> byId;
	map<string, int> byName;
	int id = 1;
	string s;
	for (int i = 0; i < n; i++) {
		cin >> s;
		byId.insert(make_pair(id, s));
		byName.insert(make_pair(s, id));
		id++;
	}
	for (int i = 0; i < m; i++) {
		cin >> s;
		if (65 <= s[0] && s[0] <= 90) {
			cout << byName[s] << '\n';
		}
		else {
			cout << byId[stoi(s)] << '\n';
		}
	}
}