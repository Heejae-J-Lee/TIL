#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

vector<int> solution(int k, vector<int> score) {
    vector<int> answer;
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for (int idx = 0; idx < score.size(); idx++){
        if (idx < k){
            pq.push(score[idx]);
        }
        else if (score[idx] <= pq.top())
        {
            /* No Action */
        }
        else {
            vector<int> st;
            
            while (!pq.empty()){
                if (score[idx] < pq.top())
                {
                    break;
                }
                st.push_back(pq.top());
                pq.pop();
            }
            
            pq.push(score[idx]);
            
            for (int j = 1; j < st.size(); j++){
                pq.push(st[j]);
            }
        }
        
        answer.push_back(pq.top());
    }
    
    return answer;
}