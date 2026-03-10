class  Father:
    def  __init__(self, fname, fage):
        self.fname = fname
        self.fage = fage
    

class Mother:
    def __init__(self, mname, mage):
        self.mname = mname
        self.mage = mage



class Child(Father,  Mother):
    def  __init__(self, name, age, fname, fage, mname, mage):

        Father.__init__(self, fname, fage)
        Mother.__init__(self, mname, mage)
        self.name = name
        self.age  = age

    def info(self):
        print(f"{self.name} is Father Name: {self.fname} Age: {self.fage} and Mother Name: {self.mname} Age: {self.mage}. He age is {self.age}.")


C = Child("kamal", 25,  "vimal", 60, "nimali", 55)

C.info()

