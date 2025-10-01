def steps(number):
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    n=number
    step_count=0
    while n>1:
        if n%2==0:
            n=n//2
        elif n%2!=0:
            n=(3*n)+1
        step_count+=1
    return step_count
        
