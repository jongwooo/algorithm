#include <iostream>
#include <string>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int month, date;
	cin >> month >> date;
	int daysInMonth[12] = { 31,28,31,30,31,30,31,31,30,31,30,31 };
	string days[7] = { "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT" };
	int totalDays = 0;
	totalDays += date;
	for (int i = 0; i < (month - 1); i++) {
		totalDays += daysInMonth[i];
	}
	cout << days[totalDays % 7];
}