#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, long long left, long long right) {
    vector<int> answer;
    
    // 0 ~ n-1
    // n ~ 2n-1
    // 2n ~ 3n-1
    // 3n ~ 4n -1
    
    // left -> (left/n, left%n)
    // right -> (right/n, right%n)
    
    for (long long i = left; i <= right; i++) {
        int col, row;
        
        col = i / n;
        row = i % n;
        
        if (row <= col) {
            answer.push_back(col+1);
        }
        else {
            answer.push_back(row+1);
        }
    }
    
    return answer;
}