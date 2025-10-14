#include <string>
#include <vector>

using namespace std;

int calculate(int a, int b) {
    return stoi(to_string(a) + to_string(b));
}

int solution(int a, int b) {
    int ab = calculate(a, b);
    if (ab < 2 * a * b) {
        return 2 * a * b;
    }
    return ab;
}