#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	int res = 0;
	while (n--) {
		int student, apple;
		cin >> student >> apple;
		res += apple % student;
	}
	cout << res;
}