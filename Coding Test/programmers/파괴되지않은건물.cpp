#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;
    
    int N = board.size();
    int M = board[0].size();
    
    vector<vector<int>> prefix_sum(N+1, vector<int>(M+1));

    for (auto s = skill.begin(); s < skill.end(); s++) {
        vector<int> skill_info = *s;
        
        int skill_type = skill_info[0];
        int r1         = skill_info[1];
        int c1         = skill_info[2];
        int r2         = skill_info[3];
        int c2         = skill_info[4];
        int degree     = skill_info[5];
        
        if (skill_type == 1) {
            degree = (-1) * degree;
        }
        
        prefix_sum[r1][c1]     += degree;
        prefix_sum[r2+1][c1]   -= degree;
        prefix_sum[r1][c2+1]   -= degree;
        prefix_sum[r2+1][c2+1] += degree;
    }
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            prefix_sum[i][j+1] += prefix_sum[i][j];
        }
    }
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            prefix_sum[j+1][i] += prefix_sum[j][i];
        }
    }
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (0 < (board[i][j] + prefix_sum[i][j])) {
                answer++;
            }
        }
    }
    
    return answer;
}
