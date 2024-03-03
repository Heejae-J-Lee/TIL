#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int s) {
    vector<int> answer;
    
    if (s < n) {
        answer.push_back(-1);
    }
    else {
        if ((s%n) == 0) {
            for (int i = 0; i < n; i++) {
                answer.push_back(s/n);
            }
        } else {
            int remain = s%n;
            for (int i = 0; i < (n-remain); i++){
                answer.push_back(s/n);
            }
            for (int i = 0; i < remain; i++){
                answer.push_back(s/n + 1);
            }
        }
    }
   
    return answer;
}