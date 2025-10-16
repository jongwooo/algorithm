#include <vector>

using namespace std;

const int INF = 1'000'001;

vector<int> solution(vector<int> arr, vector<vector<int>> queries) {
    vector<int> answer;
    int check, min;
    for (int i = 0; i < queries.size(); ++i) {
        check = 0, min = INF;
        for (int j = queries[i][0]; j <= queries[i][1]; ++j) {
            if(queries[i][2] < arr[j] && arr[j] < min) {
                min = arr[j];
                check = 1;
            }
        }
        if (check == 0) {
            min = -1;
        }
        answer.push_back(min);
    }
    return answer;
}
