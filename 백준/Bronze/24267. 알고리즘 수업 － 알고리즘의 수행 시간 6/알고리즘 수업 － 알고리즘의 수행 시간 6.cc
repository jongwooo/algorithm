#include <iostream>
using namespace std;

long n;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> n;
	cout << n * (n - 1) * (n - 2) / 6 << '\n' << 3;
}