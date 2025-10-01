def is_pangram(sentence):
    sentence=sentence.replace(" ","").lower()
    sentence=set(sentence)
    checker='abcdefghijklmnopqrstuvwxyz'
    counter=0
    for i in sentence:
        if i in checker:
            counter+=1
    return counter==26
                