class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n-1) + f(n-2)
        ways = [1, 1]
        
        for i in range(2, n+1):
            ways.append(ways[i-2] + ways[i-1])
        
        return ways[n]
