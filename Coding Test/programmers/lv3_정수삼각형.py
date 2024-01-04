def solution(triangle):
    answer = 0
    
    dp = []
    
    for i in range(1, len(triangle)+1):
        dp.append([0 for _ in range(i)])
    
    for row_index, row in enumerate(triangle):
        if row_index == 0:
            dp[0][0] = triangle[0][0]
            continue
        
        for col_index, item in enumerate(row):
            if col_index == 0:
                dp[row_index][col_index] = dp[row_index-1][col_index] + triangle[row_index][col_index]
                continue
            elif col_index == len(row)-1:
                dp[row_index][col_index] = dp[row_index-1][col_index-1] + triangle[row_index][col_index]
                continue
                
            dp[row_index][col_index] = max(dp[row_index-1][col_index], dp[row_index-1][col_index-1]) + triangle[row_index][col_index]
    
    answer = max(dp[-1])
    
    return answer
