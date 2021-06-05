class Employee:
    no_of_leaves = 9
    pass

harry = Employee()
pupun = Employee()

harry.name = "harry"
harry.sal = 700
harry.role = "instructor"

pupun.name = "rohan"
pupun.sal = 899
pupun.role = "mannager"

print(pupun.name, harry.sal)
print(harry.no_of_leaves)
print(pupun.__dict__)

print(Employee)

