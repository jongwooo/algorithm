#include <string>
#include <vector>

using namespace std;

string solution(string code) {
    int mode = 0;
    string ret = "";
    for (int idx = 0; idx < code.size(); idx++) {
        if (mode == 0) {
            if (code[idx] != '1') {
                if (idx % 2 == 0) {
                    ret += code[idx];
                }
            } else {
                mode = 1 - mode;
            }
        } else {
            if (code[idx] != '1') {
                if (idx % 2 == 1) {
                    ret += code[idx];
                }
            } else {
                mode = 1 - mode;
            }
        }
    }
    if (ret.empty()) {
        return "EMPTY";
    }
    return ret;
}
