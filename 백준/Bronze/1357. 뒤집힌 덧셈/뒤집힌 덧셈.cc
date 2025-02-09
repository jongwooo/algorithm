#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	string x;
	string y;
	cin >> x;
	cin >> y;
	reverse(x.begin(), x.end());
	reverse(y.begin(), y.end());
	int xx = stoi(x);
	int yy = stoi(y);
	int sum = xx + yy;
	string ans = to_string(sum);
	reverse(ans.begin(), ans.end());
	cout << stoi(ans);
}