#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, string> pis;

bool compare(pis p1, pis p2) {
	return p1.first > p2.first;
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	while (n--) {
		int p;
		cin >> p;
		vector<pis> v;
		while (p--) {
			int c;
			string s;
			cin >> c >> s;
			v.emplace_back(make_pair(c, s));
		}
		sort(v.begin(), v.end(), compare);
		cout << v[0].second << '\n';
	}
}