def find(search_list, value):
    search_list.sort()
    # length_of_list=len(search_list)
    # test_list=[]

    # middle=length_of_list//2
    
    # if value<search_list[middle]:
    #     for i in range (0,middle+1):
    #         test_list.append(search_list[i])
    #     if value in test_list:
    #         return test_list.index(value)
    #     else:
    #         middle=len(test_list)//2
    # else:
    #     pass

    left, right = 0, len(search_list) - 1

    while left <= right:
        middle = (left + right ) // 2

        if search_list[middle] == value:
            return middle

        if value < search_list[middle]:
            right = middle - 1
        elif value > search_list[middle]:
            left = middle + 1
            
    raise ValueError("value not in array")
        
