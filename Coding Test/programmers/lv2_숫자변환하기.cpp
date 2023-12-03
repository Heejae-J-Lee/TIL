#include <string>
#include <vector>
#include <queue>
#include <set>
#include <iostream>
using namespace std;

struct cmp {
    bool operator() (pair<int,int> a, pair<int,int> b) {
        return a.first > b.first;
    }
};

int solution(int x, int y, int n) {
    int answer = -1;
    
    priority_queue<pair<int,int>, vector<pair<int,int>>, cmp> pq;
    pq.push({0, x});
    set<int> x_set;
    
    while (!pq.empty()) {
        pair<int,int> next = pq.top();
        pq.pop();
        
        if (y < next.second) {
            continue;
        }
        else if (next.second == y) {a
            answer = next.first;
            break;
        }
        else if (next.second < y) {
            if (x_set.count(next.second * 3) == 0) {
                x_set.insert(next.second * 3);
                pq.push({next.first+1, next.second * 3});
            }
            if (x_set.count(next.second * 2) == 0) {
                x_set.insert(next.second * 2);
                pq.push({next.first+1, next.second * 2});
            }
            if (x_set.count(next.second + n) == 0) {
                x_set.insert(next.second + n);
                pq.push({next.first+1, next.second + n});
            }
        }
    }    
    
    return answer;
}