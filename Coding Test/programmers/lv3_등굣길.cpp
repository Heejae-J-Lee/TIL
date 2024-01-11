#include <string>
#include <vector>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    
    int weight[100][100] = {{0, }, };
    
    for (auto puddle = puddles.begin(); puddle < puddles.end(); puddle++) {
        weight[(*puddle)[1]-1][(*puddle)[0]-1] = -1;
    }
    
    for (int i = 0; i < m; i++) {
        if (weight[0][i] != -1)  weight[0][i] = 1;
        else {
            break;
        }
    }
    for (int i = 0; i < n; i++) {
        if (weight[i][0] != -1)  weight[i][0] = 1;
        else {
            break;
        }
    }
    
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            if (weight[i][j] != -1) {
                if (weight[i-1][j] != -1) {
                    weight[i][j] += weight[i-1][j];
                }
                
                if (weight[i][j-1] != -1) {
                    weight[i][j] += weight[i][j-1];
                }
                weight[i][j] %= 1000000007;
            }
        }
    }
    
    answer = weight[n-1][m-1];
    
    return answer;
}