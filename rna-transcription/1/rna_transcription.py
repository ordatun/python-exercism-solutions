def to_rna(dna_strand):
    rna_strand=[]
    dict = {
        "C": "G",
        "G":"C",
        "T":"A",
        "A":"U"
    }

    for strand in dna_strand:
        if strand in dict:
            rna_strand.append(dict[strand])
        

    return "".join(rna_strand)
            