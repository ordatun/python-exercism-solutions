def abbreviate(words):
    words=words.replace("-"," ").upper().replace("_"," ")
    ans=""
    for word in words.split():
        if word:
            ans+=word[0]
    
    return ans
    
