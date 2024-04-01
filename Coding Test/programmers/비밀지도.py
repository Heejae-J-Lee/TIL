def solution(n, arr1, arr2):
    answer = []
    
    map = []
    
    for row in arr1:
        code = row
        binary = ""
        while True:
            if code == 1:
                binary = "1" + binary
                binary = (n-len(binary)) * "0" + binary
                decode = binary.replace("1", "#")
                decode = decode.replace("0", " ")
                map.append(decode)
                break
            elif code == 0:
                decode = ' ' * n
                map.append(decode)
                
            binary = str(code%2) + binary
            code = code // 2
            
    for idx, row in enumerate(arr2):
        code = row
        binary = ""
        while True:
            if code == 1:
                binary = "1" + binary
                binary = (n-len(binary)) * "0" + binary
                decode = binary.replace("1", "#")
                decode = decode.replace("0", " ")
                for j, letter in enumerate(decode):
                    if letter == "#":
                        edited_row = list(map[idx])
                        edited_row[j] = "#"
                        map[idx] = ''.join(edited_row)
                break
            elif code == 0:
                break
            binary = str(code%2) + binary
            code = code // 2
    
    answer = [row for row in map]
    
    return answer
