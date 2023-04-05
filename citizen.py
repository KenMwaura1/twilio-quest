class Citizen:
    "this class is to describe a citizen of the City of Python"   
    def __init__(self, first_name, last_name): 
        self.first_name = first_name #this is an instance variable
        self.last_name = last_name
    def full_name(self):    #This is an instance method
        return self.first_name + " " + self.last_name  #This took the 2 instance variables and put them together
    greeting = "For the glory of Python!"