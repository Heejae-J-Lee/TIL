#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    
    sort(citations.rbegin(),citations.rend());
    
    for (vector<int>::iterator it = citations.begin(); it < citations.end(); it++) {
        if ((answer+1) <= *it)
            answer++;
        else 
            break;
    }
    
    return answer;
}