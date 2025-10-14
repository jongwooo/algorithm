#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    int l_size = num_list.size() - 1;
    if (num_list[l_size] > num_list[l_size - 1]) {
        num_list.push_back(num_list[l_size] - num_list[l_size - 1]);
    } else {
        num_list.push_back(num_list[l_size] * 2);
    }
    return num_list;
}
