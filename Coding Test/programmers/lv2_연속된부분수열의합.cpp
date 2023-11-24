#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> sequence, int k) {
    vector<int> answer;
    int l = 0;
    int r = 0;
    
    vector<int> partial_sums;
    
    int partial_sum = 0;
    partial_sums.push_back(partial_sum);
    
    for (auto iter = sequence.begin(); iter < sequence.end(); iter++) {
        partial_sum += *iter;
        partial_sums.push_back(partial_sum);
    }
    
    while (true) {
        if (partial_sums.size() <= r) {
            break;
        }
        int sum = partial_sums[r] - partial_sums[l];
        
        if (sum == k) {
            int answer_size = answer.size();
            if ((answer_size == 0) || ((answer_size != 0) && ((r-l-1) < (answer[1] - answer[0])))) {
                answer.clear();
                answer = {l, r-1};
            }
        }
        
        if (sum <= k) {
            r++;
        }
        else {
            l++;
        }
    }
    
    return answer;
}
