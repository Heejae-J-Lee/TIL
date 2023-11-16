#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long solution(int r1, int r2) {
    long long answer = 0;
    int y1 = r1;
    int y2 = r2;
    
    for (int x = 1; x < r2; x++) {
        while (pow(y1,2)>=(pow(r1,2)-pow(x,2))) {
            if (y1 == 0)    break;
            y1--;
        }
        while (pow(y2,2)>(pow(r2,2)-pow(x,2))) {
            if (y2 == 0)    break;
            y2--;
        }
        answer += y2-y1;
    }
    
    answer = (answer + r2-r1+1) * 4 ;
    
    return answer;
}