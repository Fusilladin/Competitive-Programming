class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    @property
    def info(self):
        return "{}s age is {}".format(self.name,self.age)

###

class Person:
    def __init__(self,name,age):
        self.info = "{}s age is {}".format(name,age)