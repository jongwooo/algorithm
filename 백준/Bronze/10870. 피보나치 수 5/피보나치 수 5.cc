#include <iostream>
using namespace std;

int fibo(int x) {
	if (x == 0 || x == 1) return x;
	return fibo(x - 2) + fibo(x - 1);

}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	cout << fibo(n);
}