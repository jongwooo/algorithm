#include <string>
#include <vector>

using namespace std;

vector<int> solution(int l, int r) {
    vector<int> answer;
    for (int n = l; n <= r; n++) {
        string num = to_string(n);
        if (n % 5 == 0) {
            int flag = 0;
            for (int i = 0; i < num.size(); i++) {
                if (num[i] != '0' && num[i] != '5') {
                    flag = 1;
                    break;
                }
            }
            if (!flag) {
                answer.push_back(n);
            }
        }
    }
    if (answer.empty()) {
        answer.push_back(-1);
    }
    return answer;
}
