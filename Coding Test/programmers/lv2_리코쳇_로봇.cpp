#include <string>
#include <vector>

using namespace std;
typedef pair<int,int> coord;
int dr[4] = {1, -1, 0, 0};
int dc[4] = {0, 0, 1, -1};

int solution(vector<string> board) {
    int answer = 0;
    
    int board_visited[100][100] = {{0,},};
    pair<int,int> board_size = {board.size(), board[0].size()};
    coord start, goal;
    
    for (auto row = 0; row < board_size.first; row++) {
        if (board[row].find('R') != -1)
            start = {row, board[row].find('R')};
        if (board[row].find('G') != -1)
            goal = {row, board[row].find('G')};
    }
    
    vector<coord> next_coords;
    next_coords.push_back(start);
    board_visited[start.first][start.second] = 1;
    
    while (!next_coords.empty()) {
        coord next = next_coords.back();
        next_coords.pop_back();
        
        int dist = board_visited[next.first][next.second] + 1;
        
        for (int idx = 0; idx < 4; idx++) {
            int index_row = next.first;
            int index_col = next.second;
            
            while (true) {
                if ((index_row + dr[idx]) < 0 || board_size.first <= (index_row + dr[idx])) {
                    break;
                }
                else {
                    if (board[index_row + dr[idx]][index_col] == 'D')    break;
                    index_row += dr[idx];
                }
                if ((index_col + dc[idx]) < 0 || board_size.second <= (index_col + dc[idx])) {
                    break;
                }
                else {
                    if (board[index_row][index_col + dc[idx]] == 'D')    break;
                    index_col += dc[idx];
                }
            }
            
            if (board_visited[index_row][index_col] != 0 && board_visited[index_row][index_col] <= dist) {
                continue;
            }
            else {
                board_visited[index_row][index_col] = dist;
                next_coords.push_back({index_row, index_col});
            }
        }
    }
    
    answer = board_visited[goal.first][goal.second] - 1;
    
    return answer;
}