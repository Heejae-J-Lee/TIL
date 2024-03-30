def seek_course(intersection, n, course, course_list):
    if len(intersection) == n:
        course_list.append(course)
    else:
        seek_course(intersection, n+1, course, course_list)
        seek_course(intersection, n+1, course+intersection[n], course_list)

def solution(orders, course):
    answer = []
    courses = set()
    
    customers = list()
    dict_num_orders = dict()
    n = len(orders)
    
    for order in orders:
        customer = set()
        for ch in order:
            customer.add(ch)
        customers.append(customer)
    
    for i in range(n):
        list_course = list()
        order_list = list(customers[i])
        order_list.sort()
        seek_course(order_list, 0, "", list_course)
        
        for course_element in list_course:
            if len(course_element) in course:
                courses.add(course_element)
                if course_element in dict_num_orders.keys():
                    dict_num_orders[course_element] += 1
                else:
                    dict_num_orders[course_element] = 1
    
    for c in course:
        check_course = []
        for item in list(courses):
            if len(item) == c:
                check_course.append(item)
                
        list_course = []
        n_max = 2
        for item in check_course:
            if n_max < dict_num_orders[item]:
                n_max = dict_num_orders[item]
                list_course = []
                list_course.append(item)
            elif n_max == dict_num_orders[item]:
                list_course.append(item)
        answer += list_course        
    
    answer.sort()
    
    return answer
