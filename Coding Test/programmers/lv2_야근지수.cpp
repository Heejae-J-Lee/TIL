#include <string>
#include <vector>
#include <queue>

using namespace std;

long long solution(int n, vector<int> works) {
    long long answer = 0;
    priority_queue<int> pq;
    
    for (auto iter = works.begin(); iter < works.end(); iter++) {
        pq.push(*iter);
    }
        
    for (int i = 0; i < n; i++) {
        if (pq.empty())    break;
        int next_work = pq.top();
        pq.pop();
        if (1 < next_work)    pq.push(next_work-1);
    }
    
    while (!pq.empty()) {
        answer += pq.top() * pq.top();
        pq.pop();
    }
    return answer;
}
