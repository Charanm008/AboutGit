class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
    def greetings(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


s1 = Student("Charan", 18, "A")
s2 = Student("John", 20, "B")
#s1.display_info()

object_list = []
object_list.append(s1)
object_list.append(s2)

for i in object_list:
    print(i.greetings())