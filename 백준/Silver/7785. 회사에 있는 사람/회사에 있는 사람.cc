#include <iostream>
#include <string>
#include <map>
#include <functional>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	string name, status;
	map <string, string, greater<string>> m;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> name >> status;
		if (status == "enter") m.insert(make_pair(name, status));
		else m.erase(name);
	}
	for (auto& p : m) {
		cout << p.first << '\n';
	}
}