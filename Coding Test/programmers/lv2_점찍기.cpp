#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long solution(int k, int d) {
    long long answer = 0;
    
    for (int i = 0; i <= d; i = i + k) {
        int y = pow(pow(d,2) - pow(i,2), 0.5);
        answer += y / k + 1;
    }
    
    return answer;
}