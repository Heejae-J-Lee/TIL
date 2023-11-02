#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    int top_priority = 0;
    int num_tasks = priorities.size();
    
    vector<int> task_performed_status(num_tasks, 0);
    int cur_task = -1;
    
    priority_queue<int> pq;
    for (int i = 0; i < num_tasks; i++) {
        pq.push(priorities[i]);
    }
    
    while (!pq.empty()) {
        top_priority = pq.top();
        pq.pop();
        
        while (true) {
            int next_task = priorities.front();
            priorities.erase(priorities.begin());
            do {
                cur_task = (cur_task+1)%num_tasks;
            } while (task_performed_status[cur_task] == 1);
            
            if (next_task == top_priority) {
                task_performed_status[cur_task] = 1;
                if (cur_task == location) {
                    for (auto it = task_performed_status.begin(); it < task_performed_status.end(); it++) {
                        if (*it == 1) {
                            answer++;
                        }
                    }

                }
                break;
            }
            else {
                priorities.push_back(next_task);
            }
        }
    }
    
    return answer;
}