def rows(letter):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l_index = alphabets.index(letter)
    max_w = 2*l_index + 1
    
    ans = []
    
    l, r = 0, max_w - 1
    while l <= r:
        row = [' '] * max_w
        row[l] = alphabets[l_index]
        row[r] = alphabets[l_index]
        ans.append("".join(row))
        
        l += 1
        r -= 1
        l_index -= 1
    
    ans_copy = ans.copy()
    ans_copy.reverse()
    
    return ans_copy+ans[1:]      
                
