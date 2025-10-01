def proteins(strand):
    protein_library={
        "AUG":"Methionine",
        "UUU":"Phenylalanine",
        "UUC":"Phenylalanine",
        "UUA":"Leucine",
        "UUG":"Leucine",
        "UCU":"Serine",
        "UCC":"Serine",
        "UCA":"Serine",
        "UCG":"Serine",
        "UAU":"Tyrosine",
        "UAC":"Tyrosine",
        "UGU":"Cysteine",
        "UGC":"Cysteine",
        "UGG":"Tryptophan",
        "UAA":"STOP",
        "UAG":"STOP",
        "UGA":"STOP"
    }

    ans_list=[]
    temp=""
    for i in range (0,len(strand), 3):
        temp = strand[i: i+3]
        if protein_library[temp]=="STOP":
            break
        else:
            ans_list.append(protein_library[temp])
        
    return ans_list