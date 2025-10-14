#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    string odd = "";
    string even = "";
    for (int i = 0; i < num_list.size(); i++) {
        if (num_list[i] % 2 == 0) {
            even += to_string(num_list[i]);
        } else {
            odd += to_string(num_list[i]);
        }
    }
    return stoi(odd) + stoi(even);
}
