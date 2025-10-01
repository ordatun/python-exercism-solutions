def is_triangle(sides):
    if 0 in sides:
        return False
    sides.sort()
    if sides[0]+sides[1]>=sides[2]:
        return True
    return False
    
def equilateral(sides):
    if is_triangle(sides):
        sides_set=set(sides)
        if len(sides_set)==1:
            return True
    return False
        
def isosceles(sides):
    if is_triangle(sides):
        sides_set=set(sides)
        if len(sides_set)==2 or len(sides_set)==1:
            return True
    return False

def scalene(sides):
    if is_triangle(sides):
        sides_set=set(sides)
        if len(sides_set)==3:
            return True
    return False
