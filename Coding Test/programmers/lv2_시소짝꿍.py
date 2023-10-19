ratios = (2/2, 3/2, 4/2, 4/3)
def solution(weights):
    answer = 0
    
    dict_weights = {}
    
    for weight in weights:
        if weight in dict_weights.keys():
            dict_weights[weight] += 1
        else:
            dict_weights[weight] = 1
    
    arr_weights = list(dict_weights.keys())
    arr_weights.sort()
    
    for i in range(0, len(arr_weights)):
        num_i = dict_weights[arr_weights[i]]
        if num_i > 1:
            answer += num_i*(num_i-1)/2
        
        for j in range(i+1, len(arr_weights)):
            ratio = arr_weights[j] / arr_weights[i]
            if ratio < 1.0:
                continue
            elif ratio > 2.0:
                break
            elif ratio in ratios:
                print(arr_weights[i], arr_weights[j])
                answer += dict_weights[arr_weights[i]] * dict_weights[arr_weights[j]]
                
    return answer