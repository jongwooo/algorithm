#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, m;
	cin >> n >> m;
	string name;
	vector<string> h, hs;
	for (int i = 0; i < n; i++) {
		cin >> name;
		h.push_back(name);
	}
	sort(h.begin(), h.end());
	for (int i = 0; i < m; i++) {
		cin >> name;
		if (binary_search(h.begin(), h.end(), name)) hs.push_back(name);
	}
	sort(hs.begin(), hs.end());
	cout << hs.size() << '\n';
	for (auto& name : hs) {
		cout << name << '\n';
	}
}