def solution(arr1, arr2):
    answer = []
    
    for row_idx, ar in enumerate(arr1):
        new_row = []
        for i in range(len(arr2[0])):
            item = 0
            for arr1_idx, arr1_item in enumerate(ar):
                item += arr1_item * arr2[arr1_idx][i]
            new_row.append(item)
        answer.append(new_row)
        
        
    return answer