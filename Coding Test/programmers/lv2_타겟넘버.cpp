#include <string>
#include <vector>
#include <queue>

using namespace std;
typedef pair<int,int> order_and_sum; // order, sum

int solution(vector<int> numbers, int target) {
    int answer = 0;
    
    queue<order_and_sum> q;
    q.push({0,0});
    
    while (!q.empty()) {
        order_and_sum next = q.front();
        q.pop();
        int next_order = next.first;
        int next_sum = next.second;
        
        if (next_order == numbers.size()) {
            if (next_sum == target)    answer++;
            continue;
        }
        q.push({next_order+1, next_sum + numbers[next_order]});
        q.push({next_order+1, next_sum - numbers[next_order]});
        
    }
    
    return answer;
}