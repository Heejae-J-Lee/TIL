def diff_time(time1, time2):
    time1_hour, time1_min = map(int, time1.split(':'))
    time2_hour, time2_min = map(int, time2.split(':'))
    
    diff_mins = (time2_hour - time1_hour) * 60 + (time2_min - time1_min)
    
    return diff_mins
    
    
def solution(fees, records):
    answer = []
    
    time_base = fees[0]
    fee_base = fees[1]
    unit_time = fees[2]
    fee_per_unit_time = fees[3]
    
    parking_lot = {}
    mins_record = {}
    
    for record in records:
        record_time, record_number, record_type = record.split()
        
        if record_type == "IN":
            parking_lot[record_number] = record_time
            
            if record_number not in mins_record.keys():
                mins_record[record_number] = 0
                
        elif record_type == "OUT":
            mins_record[record_number] += diff_time(parking_lot[record_number], record_time)
            parking_lot[record_number] = None
    
    for key in parking_lot.keys():
        if parking_lot[key] != None:
            mins_record[key] += diff_time(parking_lot[key], "23:59")
    
    cars = list(mins_record.keys())
    cars.sort()
    
    for car in cars:
        fee = fee_base
        
        use_time = mins_record[car] - time_base
        if use_time > 0:
            fee += (use_time // unit_time) * fee_per_unit_time
            print((use_time // unit_time))
            if (use_time % unit_time) > 0:
                fee += fee_per_unit_time
            
        answer.append(fee)
    
    return answer
