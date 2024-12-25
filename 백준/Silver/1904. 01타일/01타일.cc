#include <iostream>
using namespace std;

int dp[1'000'001] = { 0, };

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	dp[1] = 1, dp[2] = 2;
	for (int i = 3; i <= n; i++) {
		dp[i] = (dp[i - 2] + dp[i - 1]) % 15'746;
	}
	cout << dp[n];
}