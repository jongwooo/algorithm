#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> arr;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, tmp;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		arr.push_back(tmp);
	}
	sort(arr.begin(), arr.end());
	for (int i = 0; i < n; i++) {
		cout << arr[i] << '\n';
	}
}