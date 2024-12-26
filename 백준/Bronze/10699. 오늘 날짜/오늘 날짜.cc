#include <iostream>
#include <ctime>
#include <iomanip>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	time_t timer = time(NULL);
	struct tm *t = localtime(&timer);
	cout << t->tm_year + 1900 << '-'
		<< setw(2) << setfill('0') << t->tm_mon + 1 << '-'
		<< setw(2) << setfill('0') << t->tm_mday;
}