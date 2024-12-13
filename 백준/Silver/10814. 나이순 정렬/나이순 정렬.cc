#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

typedef pair<int, string> pis;

bool compare(pis p1, pis p2) {
	if (p1.first == p2.first) return false;
	return p1.first < p2.first;
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, age;
	string name;
	vector<pis> v;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> age >> name;
		v.push_back({ age, name });
	}
	stable_sort(v.begin(), v.end(), compare);
	for (int i = 0; i < n; i++) {
		cout << v[i].first << ' ' << v[i].second << '\n';
	}
}