#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	vector<int> v(n);
	for (int i = 0; i < n; i++) {
		cin >> v[i];
	}
	vector<int> copied(v);
	sort(copied.begin(), copied.end());
	copied.erase(unique(copied.begin(), copied.end()), copied.end());
	for (int i = 0; i < n; i++) {
		auto it = lower_bound(copied.begin(), copied.end(), v[i]);
		cout << it - copied.begin() << ' ';
	}
}