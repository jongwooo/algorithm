#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<string, int> psi;

bool compare(psi p1, psi p2) {
	return p1.second > p2.second;
}

int main() {
	cin.tie(0)->sync_with_stdio(0);
	
	int t;
	cin >> t;
	while (t--) {
		int n;
		vector<psi> v;
		cin >> n;
		while (n--) {
			string s;
			int l;
			cin >> s >> l;
			v.emplace_back(make_pair(s, l));
		}
		sort(v.begin(), v.end(), compare);
		cout << v[0].first << '\n';
	}
}