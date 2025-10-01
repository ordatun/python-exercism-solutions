def value(colors):
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
    summing=(testing[0]*10)+testing[1]
    return summing