#include <iostream>
#include <vector>
using namespace std;

int n;
int arr[100];
int cnt, sum;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	while (true) {
		cin >> n;
		if (n == -1) break;
		cnt = 0, sum = 0;
		for (int i = 1; i < n; i++) {
			if (n % i == 0) {
				arr[cnt++] = i;
				sum += i;
			}
		}
		cout << n;
		if (n == sum) {
			cout << " = ";
			for (int i = 0; i < cnt; i++) {
				cout << arr[i];
				if (i != cnt - 1) cout << " + ";
				arr[i] = 0;
			}
		}
		else cout << " is NOT perfect.";
		cout << '\n';
	}
}