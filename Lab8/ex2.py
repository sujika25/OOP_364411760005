class Person():
    def __init__(self):
        # list of attributes
        self.name = ""
        self.age = 0
        self.gender = ""

    def info(self):
        print(f'Name: {self.name} Age: {self.age} Gender: {self.gender}')

class Employee(Person): # Employee inherited from Person
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
        self.emp_id = ""
        self.position = ""

    def info(self):
        print(f'Name: {self.name} '
              f'Age: {self.age} '
              f'Gender: {self.gender} '
              f'EMP_ID: {self.emp_id} '
              f'Position: {self.position} ')


class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
        self.id = ""
        self.group = ""
        self.university = ""

    def info(self):
        print(f'Name: {self.name} '
              f'Age: {self.age} '
              f'Gender: {self.gender} '
              f'ID: {self.id} '
              f'group: {self.group} '
              f'university: {self.university}')

# create object
p1 = Person()
p1.name = "Sujika Chuaichujit"
p1.age = "21"
p1.gender = "Female"

emp1 = Employee()
emp1.name = "Piyawat Rattanaburi"
emp1.age = "19"
emp1.gender = "Male"
emp1.emp_id = "MIT431"
emp1.position = "Lecturer"

s1 = Student()
s1.name = "Sujika Chuaichujit"
s1.age = "21"
s1.gender = "Female"
s1.id = "364411760005"
s1.group = "MIT431"
s1.university = "RUTS"

s1.info()

lst = [p1,emp1,s1]

for obj in (lst):
    print(obj.__class__.__name__, end=" ")
    obj.info()

