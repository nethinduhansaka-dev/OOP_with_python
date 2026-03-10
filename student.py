class  Student:
    class_year = 2024

    number_of_students = 0


    def __init__(self, name,  age):
        self.name =  name
        self.age = age
        Student.number_of_students += 1

Student1 = Student("Alice", 20)
Student2 = Student("Bob", 22)
Student3 = Student("Charlie", 21)
Student4 = Student("Diana", 19)
Student5 = Student("Eve", 23)

print(f"{Student1.name} is {Student1.age} years old and is in class {Student1.class_year}.")
print(f"{Student2.name} is {Student2.age} years old and is in class {Student2.class_year}.")
print(f"{Student3.name} is {Student3.age} years old and is in class {Student3.class_year}.")
print(f"{Student4.name} is {Student4.age} years old and is in class {Student4.class_year}.")
print(f"{Student5.name} is {Student5.age} years old and is in class {Student5.class_year}.")

print(f"Total number of students: {Student.number_of_students}")