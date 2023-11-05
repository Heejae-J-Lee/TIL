#include <string>
#include <vector>
#include <iostream>

using namespace std;

// f(n) = f(n-1) + f(n-2)

long long solution(int n) {
    long long answer = 0;
    
    long long dp[2001] = {0,};
    dp[1] = 1;
    dp[2] = 2;
    
    for (int i = 3; i <= n; i++) {
        // dp[i] = (dp[i-1]%1234567) + (dp[i-2]%1234567);
        dp[i] = (dp[i-1] + dp[i-2])%1234567;
    }
    
    answer = dp[n];
    
    return answer;
}