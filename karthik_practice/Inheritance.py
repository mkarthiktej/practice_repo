class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    pass


x = Student("Mike", "Olsen")
x.printname()


class Details(Person):

    def __init__(self, Age, Marks):
        self.Age = Age
        self.Marks = Marks
        print(self.Age, self.Marks)


y = Details(25, 98.4)

