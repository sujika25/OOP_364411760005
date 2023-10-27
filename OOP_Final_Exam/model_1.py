class Person:

    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

    def info(self):
        print(f'Name: {self.name} '
              f'Age :  {self.age} '
              f'Email : {self.email} ')

class Student(Person):
     def __init__(self,sid,major):
        self.sid = sid
        self.major = major

     def info(self):
         print(f'Sid: {self.sid} '
               f'Major : {self.major} ')

class Employee(Person):
    def __init__(self,eid,position):
        self.eid = eid
        self.position = position

    def info(self):
        print(f'Eid: {self.eid} '
              f'Position : {self.position} ')

class Device:
    all_Devices = ["Tablet","Laptop","Mobile"]

    def __init__(self,dev_name):
        self.__dev_name = dev_name

    def get_dev_name(self):
        return self.__dev_name
    def set_dev_name(self,new_dev_name):
        self.__dev_name = new_dev_name
    def info(self):
        print(f'Device: {self.__dev_name}')

    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def info(self):
        print(f'Brand: {self.brand} '
              f'Model : {self.model} '
              f'Price: {self.price} ')

class Mobile(Device):
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def info(self):
        print(f'Brand: {self.brand} '
              f'Model : {self.model} '
              f'Price: {self.price} ')

class Tablet(Device):
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def info(self):
        print(f'Brand: {self.brand} '
              f'Model : {self.model} '
              f'Price:{self.price} ')

class Laptop(Device):
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def info(self):
        print(f'Brand: {self.brand} '
              f'Model : {self.model} '
              f'Price: {self.price} ')

class Device_Report:
    def __init__(self,Person,Student,Employee):
        self.Person = Person
        self.Student = Student
        self.Employee = Employee
        self.Device = list()


    def add_device(self,dev):
        self.Device.append(dev)

        if len(self.Device) == 0:
            print(f'\tNo device data.')
        else:
            for x in range(len(self.device)):
                print(f'\tdevice {x+1}. {self.device[x].get_dev_name()}')