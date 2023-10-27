from model_1 import Person, Student, Employee, Device, Device_Report, Tablet,Laptop, Mobile


def display_option():
    print("Welcome")
    print("1.Add user")
    print("2.Add device for user")
    print("3.Delete device for user")
    print("4.Display device information")
    print("5.Exit")


# def display_Person():
#     print("?: ")
#     n = 1
#     for x in  Device.all_Devices:
#         print(f'\t{n}. {x}')
#         n=n+1

def display_Device():
    print("How many devices do you have?: ")
    n = 1
    for x in  Device.all_Devices:
        print(f'\t{n}. {x}')
        n=n+1

name = input("Enter Person name ?: ")
age = int(input("How old are you? : "))
email = input("Enter your email ?: ")
p = Person (name,age,email)
# p.info()
sid = int(input("Enter student id? : "))
major = input("Enter your major? : ")
s = Student(id,major)
# s.info()

eid =int(input())




n = int(input("How many are you Device?: "))
for x in range(n):
    display_Device()

    v = int(input(f'select 1- {len(Device.all_Devices)}: '))
#      s_Report.add_vaccinated(Device(Device.all_Devices[v - 1]))
# s_Report.info()
#     date = input("Date(dd/mm/yyyy): ")
#     s_passport.add_date(date)
#
# s_passport.info()
# Sujika chuaichujit
# sujika.ch@rmutsvmail.com
exit()