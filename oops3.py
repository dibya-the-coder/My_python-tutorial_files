class Employee:
    no_of_leaves = 9
    def __init__(self, aname, asal, arole):
        self.name = aname
        self.sal = asal
        self.role = arole

    # def printdetails(self):
    #     return f"the name is {self.name}. salary is {self.sal}. and role is {self.role}"
harry = Employee("harry", 445, "instructor")
# harry = Employee()
# pupun = Employee()

# harry.name = "harry"
# harry.sal = 700
# harry.role = "instructor"

# pupun.name = "pupun"
# pupun.sal = 899
# pupun.role = "mannager"
print(harry.role)
