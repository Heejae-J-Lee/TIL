#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    typedef pair<int,int> price_time;
    priority_queue<price_time> pq;
    int count = -1;
    
    for (auto iter = prices.begin(); iter < prices.end(); iter++) {
        answer.push_back(0);
        count++;
        
        while (!pq.empty()) {
            price_time top_pt = pq.top();
  
            if (top_pt.first <= *iter) {
                break;
            }
            else {  
                answer[top_pt.second] = count - top_pt.second;
                pq.pop();
            }
        }
        
        price_time pt = {*iter, count};
        pq.push(pt);
    }
    
    while (!pq.empty()) {
        answer[pq.top().second] = count - pq.top().second;
        pq.pop();
    }
    
    return answer;
}