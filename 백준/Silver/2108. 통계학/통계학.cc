#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

int arr[500'000];
int freq[8'001] = { 0, };

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	double sum;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		sum += arr[i];
		freq[arr[i] + 4'000]++;
	}
	int max = freq[0];
	for (int i = 0; i < 8'001; i++) {
		if (max < freq[i]) {
			max = freq[i];
		}
	}
	vector<int> mv;
	for (int i = 0; i < 8'001; i++) {
		if (max == freq[i]) {
			mv.push_back(i - 4'000);
		}
	}
	sort(arr, arr + n);
	cout << round(sum / n) + 0.0 << '\n';
	cout << arr[n / 2] << '\n';
	cout << ((mv.size() == 1) ? mv[0] : mv[1]) << '\n';
	cout << arr[n - 1] - arr[0];
}