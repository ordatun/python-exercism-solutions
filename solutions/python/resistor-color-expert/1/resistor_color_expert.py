plus_minus = "\u00B1"
def resistor_label(colors):
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
    tolerance={
        "grey":"0.05%",
        "violet":"0.1%",
        "blue":"0.25%",
        "green":"0.5%",
        "brown":"1%",
        "red":"2%",
        "gold":"5%",
        "silver":"10%"
    }
    testing=[]
    for i in colors:
        testing.append(color_coding_library[i])
    length=len(testing)
    if length==1 and testing[0]==0:
        return f"0 ohms"
    if colors[-1] in tolerance:
        testing[-1]=tolerance[colors[-1]]
        if length==4:
            if testing[2]<2:
                 sum=((testing[0]*10)+testing[1])*(10**testing[-2])
                 return f"{sum} ohms {plus_minus}{testing[-1]}"
            if testing[2]==2:
                sum=(((testing[0]*10)+testing[1])*(10**testing[-2])/1000)
                if sum.is_integer():
                    sum=int(sum)
                else:
                    sum=float(sum)
                return f"{sum} kiloohms {plus_minus}{testing[-1]}"
            if 3<=testing[2]<=4 :
                sum=int((((testing[0]*10)+testing[1])*(10**testing[-2]))/1000)
                return f"{sum} kiloohms {plus_minus}{testing[-1]}" 
            if 5<=testing[2]<=7:
                sum=(((testing[0]*10)+testing[1])*(10**testing[-2])/(10**6))
                return f"{sum} megaohms {plus_minus}{testing[-1]}" 
            else:
                sum=(((testing[0]*10)+testing[1])*(10**testing[-2])/(10**9))
                return f"{sum} gigaohms {plus_minus}{testing[-1]}" 
        elif length==5:
            if testing[3]<1:
                 sum=((testing[0]*100)+testing[1]*10+testing[2])*(10**testing[-2])
                 return f"{sum} ohms {plus_minus}{testing[-1]}"
            if testing[3]==1:
                sum=(((testing[0]*100)+testing[1]*10+testing[2])*(10**testing[-2])/1000)
                return f"{sum} kiloohms {plus_minus}{testing[-1]}" 
            if 2<=testing[3]<=3:
                sum=int((((testing[0]*100)+testing[1]*10+testing[2])*(10**testing[-2]))/1000)
                return f"{sum} kiloohms {plus_minus}{testing[-1]}" 
            if 4<=testing[3]<=6:
                sum=(((testing[0]*100)+testing[1]*10+testing[2])*(10**testing[-2])/(10**6))
                return f"{sum} megaohms {plus_minus}{testing[-1]}" 
            else:
                sum=(((testing[0]*100)+testing[1]*10+testing[2])/(10**9))
                return f"{sum} gigaohms {plus_minus}{testing[-1]}"

