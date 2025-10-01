def is_armstrong_number(number):
    digits=len(str(number))
    sum=0
    for digit in str(number):
        sum+=int(digit)**digits
    return number == sum
