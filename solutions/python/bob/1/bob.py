def response(hey_bob):
    n=hey_bob.strip()
    answer=''

    if n=='':
        return 'Fine. Be that way!'
    elif n[-1]=='?':
        if n.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return 'Sure.'  
    elif n.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'

        