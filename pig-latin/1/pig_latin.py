def translate(text):
    vowels = ["a", "e", "i", "o", "u","y"]
    translated_words = []
    words = text.lower().split()
    
    for word in words:
        if word[0] not in vowels:
            for i in range(len(word)):
                if word[i] in vowels:
                    if word[i]=="u":
                        if word[i-1]=="q":
                            temp=word[:i+1]
                            word=word[i+1:]+temp+"ay"
                        else:
                            temp=word[:i]
                            word = word[i:] + temp + "ay"
                        break
        
                    else:
                        temp = word[:i]
                        if temp == "xr" or temp == "yt":
                            word = word + "ay"
                        else:
                            word = word[i:] + temp + "ay"
                        break
        elif word[0]=="y":
            if word[1] not in vowels:
                word=word+"ay"
            else:
                temp=word[1:]
                word=temp+"yay"
            
        else:
            word = word + "ay"
        
        
        translated_words.append(word)
    

    return " ".join(translated_words)

            
        
        
