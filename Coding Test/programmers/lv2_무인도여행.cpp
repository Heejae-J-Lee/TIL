#include <string>
#include <vector>
#include <algorithm>

#include <iostream>

using namespace std;

int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};
typedef pair<int,int> loc;

vector<int> solution(vector<string> maps) {
    vector<int> answer;
    int size;
    
    for (int r = 0; r < maps.size(); r++) {
        for (int c = 0; c < maps[0].length(); c++) {
            vector<loc> st;
            size = 0;
            if (maps[r][c] != 'X') {
                loc coord = {r,c};
                size += int(maps[r][c]-'0');
                maps[r][c] = 'X';
                st.push_back(coord);
            }
            while (!st.empty()) {
                loc cur = st.back();
                st.pop_back();
                
                for (int d = 0; d <= 4; d++) {
                    pair<int,int> next = {cur.first + dr[d], cur.second + dc[d]};
                    if ( (next.first < 0) || (maps.size() <= next.first) || (next.second < 0) || (maps[0].length() <= next.second)) {
                        continue;
                    }
                    else {
                        if (maps[next.first][next.second] != 'X') {
                            st.push_back(next);
                            size += int(maps[next.first][next.second] - '0');
                            maps[next.first][next.second] = 'X';
                        }
                    }
                }
            }
            if (size != 0) answer.push_back(size);
        }
    }
    
    if (answer.size() == 0) {
        answer.push_back(-1);
    }
    else {
        sort(answer.begin(), answer.end());
    }
    
    return answer;
}