#include <iostream>
#include <algorithm>
#define MAX 100'001
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	int arr[MAX];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	int dp[MAX];
	dp[0] = arr[0];
	for (int i = 1; i < n; i++) {
		dp[i] = max({ arr[i], arr[i] + dp[i - 1] });
	}
	cout << *max_element(dp, dp + n);
}