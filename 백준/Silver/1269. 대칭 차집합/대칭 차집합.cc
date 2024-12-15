#include <iostream>
#include <algorithm>
#include <set>
#include <iterator>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, m;
	cin >> n >> m;
	set<int> a, b;
	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		a.emplace(num);
	}
	for (int i = 0; i < m; i++) {
		int num;
		cin >> num;
		b.emplace(num);
	}
	set<int> ab, ba;
	set_difference(a.begin(), a.end(), b.begin(), b.end(), inserter(ab, ab.begin()));
	set_difference(b.begin(), b.end(), a.begin(), a.end(), inserter(ba, ba.begin()));
	cout << ab.size() + ba.size();
}