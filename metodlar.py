

class Animal:
    def __init__(self):
        print("animal created")
    def toString(self):
        print("animal")
        
       
    def walk(self):
        print("walk")
               
    
    
class Monkey(Animal):
    def __init__(self):
        
       super().__init__()
       print("monkey is  created")
    
    def toString(self):
        print("monkey")
        
    def climb(self):
        print("monkey can climb")
        
m1=Monkey()

