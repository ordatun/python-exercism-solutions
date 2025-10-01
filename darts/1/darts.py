import math
def score(x, y):
    radius = math.sqrt(x**2+y**2)
    if radius>10:
        return 0
    elif radius<=10 and radius>5:
        return 1
    elif radius<=5 and radius>1:
        return 5
    else:
        return 10
