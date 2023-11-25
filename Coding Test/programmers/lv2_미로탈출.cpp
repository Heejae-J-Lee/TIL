#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <iostream>
using namespace std;

int dr[4] = {1, -1, 0, 0};
int dc[4] = {0, 0, 1, -1};

typedef pair<int,int> coord;
typedef pair<coord, int> path_log;

struct cmp {
    bool operator()(path_log a, path_log b) {
        return a.second > b.second;
    }
};

int seek_path(vector<string> maps, coord start_point, char seek_letter) {
    int visited[100][100] = {{0,},};
    int size_row = maps.size();
    int size_col = maps[0].size();
    
    priority_queue<path_log, vector<path_log>, cmp> pq;
    pq.push({start_point, 0});
    visited[start_point.first][start_point.second] = 1;
    
    while (!pq.empty()) {
        coord pos = pq.top().first;
        int pos_row = pos.first;;
        int pos_col = pos.second;
        int dist = pq.top().second;
        pq.pop();
       
        for (int i = 0; i < 4; i++) {
            int pos_next_row = pos_row + dr[i];
            int pos_next_col = pos_col + dc[i];
            
            if ((pos_next_row < 0) || (size_row <= pos_next_row) || (pos_next_col < 0) || (size_col <= pos_next_col)) {
                continue;
            }
            
            if ((maps[pos_next_row][pos_next_col] != 'X') && (visited[pos_next_row][pos_next_col] == 0)) {
                if (maps[pos_next_row][pos_next_col] == seek_letter) {
                    return (dist+1);
                }
                visited[pos_next_row][pos_next_col] = 1;
                pq.push({{pos_next_row, pos_next_col}, dist+1});
            }    
        }
    }
    
    return 0;
}

int solution(vector<string> maps) {
    int answer = 0;
    
    coord start, end, lever;
    int row_cnt = 0;
    
    for (auto iter_row = maps.begin(); iter_row < maps.end(); iter_row++) {
        string::size_type S_pos = (*iter_row).find("S");
        string::size_type L_pos = (*iter_row).find("L");
        
        if (S_pos != string::npos) {
            start = {row_cnt, (int) S_pos};
        }
        
        if (L_pos != string::npos) {
            lever = {row_cnt, (int) L_pos};
        }
        
        row_cnt++;
    }
    
    int start_to_lever = seek_path(maps, start, 'L');
    if (start_to_lever != 0) {
        answer += start_to_lever;
    }
    else {
        return -1;
    }
    
    int lever_to_end = seek_path(maps, lever, 'E');
    if (lever_to_end != 0) {
        answer += lever_to_end;
    }
    else {
        return -1;
    }
    
    return answer;
}
