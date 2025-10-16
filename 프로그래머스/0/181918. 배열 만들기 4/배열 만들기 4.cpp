#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> stk;
    int i = 0;
    while (i < arr.size()) {
        if (stk.empty()) {
            stk.push_back(arr[i]);
            i++;
        } else if (stk[stk.size() - 1] < arr[i]) {
            stk.push_back(arr[i]);
            i++;
        } else {
            stk.pop_back();
        }
    }
    return stk;
}
