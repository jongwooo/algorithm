#include <iostream>
#include <string>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	string s;
	cin >> s;
	double grade;
	if (s[0] == 'A') grade = 4;
	else if (s[0] == 'B') grade = 3;
	else if (s[0] == 'C') grade = 2;
	else if (s[0] == 'D') grade = 1;
	else grade = 0;
	if (s[1] == '+') grade += 0.3;
	else if (s[1] == '-') grade -= 0.3;
	cout << fixed;
	cout.precision(1);
	cout << grade;
}