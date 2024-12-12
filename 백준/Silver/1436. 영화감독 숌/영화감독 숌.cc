#include <iostream>
#include<string>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	int num = 1, cnt = 1;
	while (true) {
		if (to_string(num).find("666") != string::npos) {
			if (n == cnt) {
				cout << num;
				break;
			}
			cnt++;
		}
		num++;
	}
}