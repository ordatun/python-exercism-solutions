import random
import string

class Robot:
    used_names = set()  

    def __init__(self):
        self.reset() 
    def reset(self):
        
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            numbers = ''.join(random.choices(string.digits, k=3))
            new_name = letters + numbers
           
            if new_name not in Robot.used_names:
                Robot.used_names.add(new_name)  
                self.name = new_name
                break

robot=Robot()       
print(robot.name)
        
        