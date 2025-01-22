#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int a, b;
	cin >> a >> b;
	int idx = 0;
	int arr[1'001];
	for (int i = 1; i <= b; i++) {
		for (int j = 0; j < i; j++) {
			if (idx > 1'000) break;
			arr[idx++] = i;
		}
	}
	int sum = 0;
	for (int i = a - 1; i < b; i++) {
		sum += arr[i];
	}
	cout << sum;
}