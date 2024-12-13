#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;

bool compare(pii p1, pii p2) {
	if (p1.second == p2.second) return p1.first < p2.first;
	return p1.second < p2.second;
}

int main() {
	cin.tie(0)->sync_with_stdio(0);
	
	int n, x, y;
	vector<pii> v;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> x >> y;
		v.push_back({ x, y });
	}
	sort(v.begin(), v.end(), compare);
	for (int i = 0; i < n; i++) {
		cout << v[i].first << ' ' << v[i].second << '\n';
	}
}