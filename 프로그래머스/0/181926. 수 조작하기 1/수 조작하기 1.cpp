#include <string>

using namespace std;

int solution(int n, string control) {
    for (int i = 0; i < control.size(); i++) {
        if (control[i] == 'w') {
            n++;
        } else if (control[i] == 's') {
            n--;
        } else if (control[i] == 'd') {
            n += 10;
        } else if (control[i] == 'a') {
            n -= 10;
        }
    }
    return n;
}
