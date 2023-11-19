#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int f[2] = {0, 1};
    int cnt = 1;
    
    while (true) {
        if (cnt == n)    break;
        cnt++;
        
        answer = (f[0] + f[1]) % 1234567;
        f[0] = f[1];
        f[1] = answer;
    }
    
    answer = f[1];
    
    return answer;
}