class Animal(): #Super Class
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def breathe(self):
        print("animal " + self.name + " requested breathe")

    def eat(self):
        print("animal " + self.name + " requested eat")

    def sleep(self):
        print("animal " + self.name + " requested sleep")


class Cat(Animal): #Subclass 1
    def __init__(self, breed, color, name, age):
        super().__init__(name, age)
        self.breed = breed
        self.color = color
    
    def purr(self):
        
        print("cat (extending animal) with name " + self.name + " requested purr")

    def breathe(self):
        print("cat (extending animal) " + self.name + " requested breathe")

class Dog(Animal): #Subclass 2
    def __init__(self, breed, color, name, age): 
        super().__init__(name, age)
        self.breed = breed
        self.color = color
    
    def bark(self):
        print("dog (extending animal) with name " + self.name + " requested bark")


