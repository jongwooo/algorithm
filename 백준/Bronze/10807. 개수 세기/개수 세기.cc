#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	int arr[101];
	int v;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	cin >> v;

	int ans = 0;
	for (int i = 0; i < n; i++) {
		if (arr[i] == v) {
			ans++;
		}
	}

	cout << ans;
}