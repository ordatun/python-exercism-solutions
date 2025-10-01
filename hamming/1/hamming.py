def distance(strand_a, strand_b):
    counter=0
    if len(strand_a)==len(strand_b):
        for i in range (0,len(strand_a)):
            if strand_a[i]==strand_b[i]:
                counter+=1
        return (len(strand_a)-counter)
    else:
        raise ValueError("Strands must be of equal length.")
