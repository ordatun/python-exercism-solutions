import math

def cipher_text(plain_text):        
    plain_text = plain_text.replace(" ","").lower()
    for n in plain_text:
        if not n.isalnum():
            plain_text = plain_text.replace(n,"")

    if not plain_text:
        return ""
        
    column=math.ceil(math.sqrt(len(plain_text)))
    row=math.ceil(len(plain_text)/column)
    
    sub_texts = []
    for i in range(row):
        temp = plain_text[:column]
        sub_texts.append(temp)
        plain_text = plain_text[column:]
        
    if (len(sub_texts[-1]) < column):
        sub_texts[-1] += " " * (column - len(sub_texts[-1]))
    
    ans = ""
    for j in range(column):
        for t in sub_texts:
            ans += t[j]
    
    sub_texts = []
    for i in range(column):
        temp = ans[:row]
        sub_texts.append(temp)
        ans = ans[row:]

    if (len(sub_texts[-1]) < row):
        sub_texts[-1] += " " * (row - len(sub_texts[-1]))
        
    return " ".join(sub_texts)