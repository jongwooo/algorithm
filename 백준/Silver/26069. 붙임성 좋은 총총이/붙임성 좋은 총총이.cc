#include <iostream>
#include <string>
#include <set>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	string a, b;
	set<string> s;
	s.emplace("ChongChong");
	while (n--) {
		cin >> a >> b;
		if (s.find(a) != s.end()) {
			s.emplace(b);
		}
		else if (s.find(b) != s.end()) {
			s.emplace(a);
		}
	}
	cout << s.size();
}