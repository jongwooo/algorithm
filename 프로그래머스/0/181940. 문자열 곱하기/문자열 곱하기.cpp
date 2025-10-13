#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int k) {
    string answer = "";
    while (k > 0) {
        answer += my_string;
        k--;
    }
    return answer;
}