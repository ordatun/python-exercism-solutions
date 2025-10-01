def label(colors):
    color_coding_library={
        "black":0,
        "brown":1,
        "red":2,
        "orange":3,
        "yellow":4,
        "green":5,
        "blue":6,
        "violet":7,
        "grey":8,
        "white":9
    }
    testing=[]
    for i in colors:
        testing.append(color_coding_library[i])
    
    if testing[2]<2:
         sum=((testing[0]*10)+testing[1])*(10**testing[2])
         return f"{sum} ohms"
    if 2<=testing[2]<=4 :
        sum=int((((testing[0]*10)+testing[1])*(10**testing[2]))/1000)
        return f"{sum} kiloohms" 
    if 5<=testing[2]<=7:
        sum=int((((testing[0]*10)+testing[1])*(10**testing[2]))/(10**6))
        return f"{sum} megaohms" 
    else:
        sum=int((((testing[0]*10)+testing[1])*(10**testing[2]))/(10**9))
        return f"{sum} gigaohms" 
        