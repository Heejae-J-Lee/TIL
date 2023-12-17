#include<vector>
#include<queue>

using namespace std;
typedef pair <int, int> location;
typedef pair<location, int> weight;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int solution(vector<vector<int> > maps)
{
    int answer = -1;
    
    int visited[100][100] = {{0,},};
    queue<weight> q;
    location goal = {maps.size() - 1, maps[0].size() - 1};
    
    q.push({{0,0}, 1});
    visited[0][0] = 1;
    
    while (!q.empty()) {
        weight next_item = q.front();
        location loc = next_item.first;
        int dist = next_item.second;
        q.pop();
        
        if ((loc.first == goal.first) && (loc.second == goal.second)) {
            answer = dist;
            break;
        }
        
        for (int i = 0; i < 4; i++) {
            int next_y = loc.first + dy[i];
            int next_x = loc.second + dx[i];
            
            if ((next_y < 0) || (goal.first < next_y))    continue;
            if ((next_x < 0) || (goal.second < next_x))    continue;
            if ((visited[next_y][next_x] == 1) ||(maps[next_y][next_x] == 0))    continue;
            
            visited[next_y][next_x] = 1;
            q.push({{next_y, next_x}, dist+1});
        }
    }
    
    return answer;
}