def solution(want, number, discount):
    answer = 0
    
    buy_list = dict()
    bucket_size = 0
    
    for idx, item in enumerate(want):
        buy_list[item] = number[idx]
        bucket_size += number[idx]
    
    bucket = []
    for discount_item in discount:
        if discount_item in buy_list.keys():
            if bucket.count(discount_item) < buy_list[discount_item]:
                bucket.append(discount_item)
                if len(bucket) == bucket_size:
                    answer += 1
                    bucket.pop(0)
            else:
                while bucket[0] != discount_item:
                    bucket.pop(0)
                bucket.pop(0)
                bucket.append(discount_item)
        else:
            bucket = []
    return answer