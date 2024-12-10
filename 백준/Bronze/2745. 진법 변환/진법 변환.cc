#include <iostream>
#include <string>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	string n;
	int b, num = 0;

	cin >> n >> b;

	for (int i = 0; i < n.length(); i++) {
		if ('0' <= n[i] && n[i] <= '9') {
			num = num * b + (n[i] - '0');
		}
		else {
			num = num * b + (n[i] - 'A' + 10);
		}
		
	}

	cout << num;
}