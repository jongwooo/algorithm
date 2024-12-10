#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, b;

	cin >> n >> b;

	string temp;
	int remain;
	while (n != 0) {
		remain = n % b;
		if (0 <= remain && remain <= 9) {
			temp += remain + '0';
		}
		else {
			temp += remain - 10 + 'A';
		}
		n /= b;
	}
	reverse(temp.begin(), temp.end());

	cout << temp;
}