#include <iostream>
#include <vector>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int a, b;
	cin >> a >> b;
	vector<int> v;
	for (int i = 1; i <= b; i++) {
		for (int j = 0; j < i; j++) {
			v.emplace_back(i);
		}
	}
	int sum = 0;
	for (int i = a - 1; i < b; i++) {
		sum += v[i];
	}
	cout << sum;
}