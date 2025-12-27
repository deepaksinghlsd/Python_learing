# Polymorphism in python : 
# Same method name in different classes with different implementations .

class Animal : 
    def speak(self) :
        print(f"The animal makes a sound .")

class Dog (Animal) :
    def speak(self) :
        print(f"The dog barks .")

def make_animal_speak(animal) :
    animal.speak()
animal1 = Animal()
animal2 = Dog()

make_animal_speak(animal1)  # Output : The animal makes a sound .
make_animal_speak(animal2)  # Output : The dog barks .

# Encapsulation in python : 
# Warping data and methods into a single unit and restricting access to some components .
class BankAccount :
    def __init__ (self , accounct_number, balance) :
        self.__account_number = accounct_number # Private attrubute 
        self.__balance = balance # private attribute 

    def deposit(self , amount ) :
            if amount > 0 :
                self.__balance += amount 
                print(f"Deposited {amount} . New balance is {self.__balance}.")
    def withdraw (self , amount ) :
                    if 0 < amount <= self.__balance :
                        self.__balance -= amount 
                        print(f"Withdrawn {amount } . New balance is {self.__balance} .")

account = BankAccount("123456789" , 1000)
account.deposit(500)
account.withdraw(200)

# Abstraction in python :
from abc import ABC , abstractmethod
class Shape (ABC) :
     @abstractmethod
     def area(self) :
          pass
    
class Rectangle (Shape) :
        def __init__ (self , width , height) :
            self.width = width 
            self.height = height 
        def area(self) :
            return self.width * self.height
        
rect = Rectangle(5 , 10)
print(f"Area of rectangle : {rect.area()}")