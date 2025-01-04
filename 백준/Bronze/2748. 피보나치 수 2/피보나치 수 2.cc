#include <iostream>
#define MAX 91
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	long long dp[MAX] = { 0, 1, 1 };
	int n;
	cin >> n;
	for (int i = 3; i <= n; i++) {
		dp[i] = dp[i - 1] + dp[i - 2];
	}
	cout << dp[n];
}