def is_isogram(string):
    
    string=string.lower()
    string=string.replace("-", "").replace(" ", "")

    # return len(set(string)) == len(string)
    
    counter=0
    for i in range(0,len(string),1):
        for j in range(i+1,len(string),1):
            if string[i]==string[j]:
                counter+=1

    return counter == 0
