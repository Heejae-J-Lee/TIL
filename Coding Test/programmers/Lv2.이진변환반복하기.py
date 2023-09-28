def binary_transform(string):
    removed_zeros = string.replace("0", "")
    string_size_removed_zeros = len(removed_zeros)
    return "{0:b}".format(string_size_removed_zeros)

def solution(s):
    answer = [0, 0]
    
    while True:
        if s == "1":
            break
        answer[0] += 1
        answer[1] += s.count("0")
        s = binary_transform(s)
    
    return answer
