#include <iostream>
#include <string>
#include <set>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, cnt = 0;
	set<string> s;
	string str;
	cin >> n;
	while (n--) {
		cin >> str;
		if (str == "ENTER") {
			cnt += s.size();
			s.clear();
			continue;
		}
		s.emplace(str);
	}
	cnt += s.size();
	cout << cnt;
}