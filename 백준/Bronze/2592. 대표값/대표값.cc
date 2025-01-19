#include <iostream>
using namespace std;

int arr[1'001];

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int max = 0, cnt = 0;
	int sum = 0;
	for (int i = 0; i < 10; i++) {
		int num;
		cin >> num;
		sum += num;
		arr[num]++;
		if (cnt < arr[num]) {
			cnt = arr[num];
			max = num;
		}
	}
	cout << sum / 10 << '\n' << max;
}