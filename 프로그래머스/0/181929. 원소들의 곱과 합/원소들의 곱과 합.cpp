#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int product = 1;
    int sum = 0;
    for (int i = 0; i < num_list.size(); i++) {
        product *= num_list[i];
        sum += num_list[i];
    }
    if (product < sum * sum) {
        return 1;
    }
    return 0;
}
