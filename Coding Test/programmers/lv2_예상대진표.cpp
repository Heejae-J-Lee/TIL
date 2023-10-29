#include <iostream>

using namespace std;

int solution(int n, int a, int b)
{
    int answer = 0;
    int p1, p2;
    
    if (a<b){
        p1 = a;
        p2 = b;
    }
    else {
        p1 = b;
        p2 = a;
    }
    
    while (n != 1) {
        answer++;
        if ((p2 % 2 == 0) && (p2==p1+1)) {
            break;
        }
        n /= 2;
        p1 -= (p1 / 2);
        p2 -= (p2 / 2);
    }
    
    
    return answer;
}