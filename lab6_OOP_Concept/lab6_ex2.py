class Student:
 def __init__(self):
    self.name = ""
    self.major = ""
    self.gpa = 0

    # display Pobject attribute
 def sudent_info(self):
    print(f'name:{self.name} major:{self.major} gpa:{self.gpa}')


s1 = Student() #empty object
#assing data Pto object attribute
s1.name = "Film"
s1.major = "MIT"
s1.gpa = 3.0

#display student data
s1.sudent_info()

# get data from user
# s2 = Student()
# s2.name = input("Enter name: ")
# s2.major = input("Enter major: ")
# s2.gpa = float(input("Enter gpa: "))
# s2.Student_info()

std = []
n = int(input('How many Student? : '))
for i in range(n):
    s = Student()
    print(f"Please, enter student info {i+1}:")
    s.name = input("Enter name: ")
    s.major = input("Enter major: ")
    s.gpa = float(input("Enter gpa: "))
    std.append(s)


# display call student in list
for i in std:
    i.student_info()