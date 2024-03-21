#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == ' ') {
            answer += s[i];
        }
        else if (('a' <= s[i]) && (s[i] <= 'z')) {
            char letter = 'a' + ((s[i] - 'a' + n) % 26);
            answer += letter;
        }
        else if (('A' <= s[i]) && (s[i] <= 'Z')) {
            char letter = 'A' + ((s[i] - 'A' + n) % 26);
            answer += letter;
        }
    }
    
    return answer;
}
