#include <string>
#include <vector>

using namespace std;

string solution(vector<int> numLog) {
    string result = "";
    for (int i = 1; i < numLog.size(); i++) {
        int diff = numLog[i] - numLog[i - 1];
        if (diff == 1) {
            result += 'w';
        } else if (diff == -1) {
            result += 's';
        } else if (diff == 10) {
            result += 'd';
        } else if (diff == -10) {
            result += 'a';
        }
    }
    return result;
}
