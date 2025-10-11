#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n, int w, int num) {
    int cnt = 0;
    while (num <= n) {
        num += (w - ((num - 1) % w) - 1) * 2 + 1;
        cnt++;
    }
    return cnt;
}