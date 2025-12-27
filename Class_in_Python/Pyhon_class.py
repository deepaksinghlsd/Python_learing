class persion :
    def __init__ (self, name , age , city , country , profession) :
        self.name = name 
        self.age = age 
        self.city = city 
        self.country = country 
        self.profession = profession 
    def introduce_yourself(self) :
            print(f"Hello , My name is {self.name} , I am {self.age} years old , I live in {self.city } , {self.country} and I workd ad a {self.profession} .")


name = input("Enter your name :")
age = int(input("Enter your age :"))
city = input("Enter Your city :")
country = input("Enter your country :")
profession = input("Enter your profession :")
person1 = persion(name , age , city , country , profession)

person1.introduce_yourself()

print(f"person details : {vars(person1)}")

# vars() function is used to return the __dict__ attribute of the given object . It returns a dictionary representation of the object's attributes and their values .

# __init__() method is also known as the constructor of the class .

# __init__() method is a special method in python classes that is called when an object is instantiated from the class . It is 
# used to initialize the attributes of the object . The __init__() method takes self as the first parameter , which refers to the instance of the 
# class being created , followed by any other parameters needed to intialize the object's attributes .



# self parameter in python class  is a reference to the current instance of the class . It is used to acces variables and methods associated with the class instance .


# When a method is called on an object , the object itself is passed as the first argument to the method , which is conventionally,named self .


# opps concepts : Object Oriented Programing concepts :
# 1 . Class : A calss is a blueprint for creating objects . It defines a set of attributes and methods that the created objects will have .
# 2 . Object : An object is an instance of a class . It is created using the class blueprint and can have its own unique attributes and behaviors . 
# 3 . Inheritance : Inheritance is a mechanism that allows a class to inherit attributes and methods from another class . This promotes code reusability and establishes a hierarchical relationship between classes .
# 4 . Polymorphism : Polymorphism allowa methos to do different things based on the object it is acting upon . It allows methods to be used in different ways depending on the context .
# 5 . Encapsulation : Encapsulation is the bundling of data (attributes) and methods (functions) that operate on that data into a single unit or class . It restricts direct access to some of the object's componets , which helps to prevent unintende interference and misuse of the data .
# 6 . Abstraction : Abstraction is the process of simplifying complex systems by hiding unnecessary details and exposing only the essential features . It alloes programers to focus on high- level concepts without getting bogged down by low-level implementation detailes .

# Inheritance --- ------> 
class Employee (persion) :
    def __init__ (self, name , age , city , country , profession , employee_id , salary) :
        super().__init__(name , age , city , country , profession)
        self.employee_id = employee_id 
        self.salary = salary 
    def display_employee_details(self) :
        print(f"Employee ID : {self.employee_id} , Salary : {self.salary} ") 
       

 
employee_1 = Employee("John Doe" , 30 , "New York" , "USA" , "Software Engineer" , "E12345" , 80000)
employee_1.display_employee_details()

       

        # super() function is used to call a method from the parent calss . It allowa us to access methods and attributes of the parent class from the child class .
        # It is commonly used in inheritannce to ensure that the parent class is properly initialized when creating an instance of the child class .
        # chid class can use parent class methods and attributes using super() function .

        

