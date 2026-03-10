class  Father:
    def  skills1(self):
        print("Father Skills: Gardening")

class  Mother:
    def  skills2(self):
        print("Mother Skills: Cooking")

class Child(Father,  Mother):
    def  skills3(self):
        print("Child  skill:  Programming")


C  =  Child()

C.skills1()
C.skills2()
C.skills3()