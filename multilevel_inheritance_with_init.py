class Grandfather:
    def __init__(self, gname):
        self.gname  = gname

class Father(Grandfather):
    def __init__(self,  gname, fname):
        super().__init__(gname)
        self.fname =  fname

class Child(Father):
    def  __init__(self, name, fname, gname ):
        super().__init__(gname, fname)
        self.name  = name

    def info(self):
        print(f"My  Name  is  {self.name}. My  Father  Name is  {self.fname} and Grand Father Name  is {self.gname}.")

c = Child('Damith', "Sumana siri", "dadli")

c.info()