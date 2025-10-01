def commands(binary_str):
    data_array=["jump","close your eyes","double blink","wink"]
    result_array=[]
    for i in range(-1,-(len(binary_str)),-1):
        if binary_str[i]=="1":
            result_array.append(data_array[i])
    if binary_str[0]=="1":
        result_array.reverse()
    return result_array
            
