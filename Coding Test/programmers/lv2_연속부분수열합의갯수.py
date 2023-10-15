def solution(elements):
    answer = 0
    size_elements = len(elements)
    
    sums_array = []
    sums = 0
    for element in elements:
        sums += element
        sums_array.append(sums)
        
    my_set = set()
    for base in range(0, size_elements):
        for length in range(0, size_elements):
            sums = 0
            
            if base == 0:
                sums_base = 0
            else: 
                sums_base = sums_array[base-1]
                
            if base+length < size_elements:
                sums = sums_array[base+length] - sums_base
            else:
                sums = sums_array[-1] - sums_base + sums_array[(base+length)%size_elements]
                
                
            my_set.add(sums)
    
    return len(my_set)