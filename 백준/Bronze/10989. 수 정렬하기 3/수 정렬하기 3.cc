#include <iostream>
using namespace std;

int arr[10'001] = { 0, };

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, tmp;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		arr[tmp]++;
	}
	for (int i = 1; i <= 10'000; i++) {
		for (int j = 0; j < arr[i]; j++) {
			cout << i << '\n';
		}
	}
}