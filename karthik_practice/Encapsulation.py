class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print("name is ", self.name, "salary is ", self.__salary)

    # @property
    # def salary(self):
    #     return self._salary
    def getsalary(self):
        print(self)

    def setsalary(self, sealary):
        print(self)


emp = Employee("karthik", 40000)
emp.show()

emp.setsalary(1000)
emp.getsalary()
