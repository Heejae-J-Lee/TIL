#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    
    vector<int> line[20000];
    int dists[20000] = {0,};
    dists[0] = 1;
    queue<pair<int, int>> next_edges;
    next_edges.push({0, 1});
    
    for (auto iter = edge.begin(); iter < edge.end(); iter++) {
        int edge_one = (*iter)[0]-1;
        int edge_two = (*iter)[1]-1;
        
        line[edge_one].push_back(edge_two);
        line[edge_two].push_back(edge_one);
    }
    
    while (true) {
        if (next_edges.size() == 0) {
            break;
        }
        
        pair<int,int> next_edge = next_edges.front();
        int e = next_edge.first;
        int dist = next_edge.second + 1;
        next_edges.pop();
        
        for (auto iter = line[e].begin(); iter < line[e].end(); iter++) {
            if (dists[(*iter)] != 0) {
                continue;
            }
            else {
                dists[(*iter)] = dist;
                next_edges.push({(*iter), dist});
            }
        }       
    }
    
    int max_dist = 0;
    for (int i = 0; i < n; i++){
        if ( max_dist < dists[i]) {
            max_dist = dists[i];
            answer = 1;
        }
        else if (max_dist == dists[i]) {
            answer++;
        }
    }
    
    return answer;
}
