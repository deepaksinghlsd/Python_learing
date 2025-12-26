name_list = ["deepak" , "shibham , rahual", "arun"]
print(f"name of these list are :{name_list}")

for name in name_list :
    print(f"Name is : {name}")

    print (f"Length of list name is : {len(name_list)}")

# List  = In python liat are used to store multiple itmes in a single variblale . and liast are mutable which 
# means we can change the values of liast after its creation . we can add , remove or modify items in a list .

# Tuples : In python tuples are used to store multiples items in a single variable and tuples are immutable 
# which means we cannot change the values of tuples after its creation . we cannot add , remove or modify items in a tuple .
# list are defined using square brackets [], and tuples are defined using parentheses() .

# examples of tuples : - 

my_tuples = ("apples" , "banana" , 12345 , True , 67.258 , 'apples')
for item in my_tuples : 
    print(f"Item in tuples are : {item}")

print(f"Length of tuples is : {len(my_tuples)}")

# Difference between list and tuples : - 
# 1. Mutability : List are mutable , while tuples are immutable .
# 2. syntax : List are defined using square brackets [] ,  while tuples are defines using parentheses () .
# 3. Performance : Tuples are generally faster than list because of their immutability .
# 4. Use case : List are used when we need a collection of items that may change ,while tuples are used when we need a collection of item that should not channge .

# Dictionary : --------------------->

# in python dictionary are used to store key-value pairs . each key is unique and is used to acces the corresponding value .
# Dictionaries are mutable , which means we can change the values of dictionary after its creation , we can add , remove or modify items in a dictionary . 
# Dictionaries are defined using curly braces {} .
# example of dictionary : - 

my_dict = {
    'name' : 'Deepak Singh' ,
    'age' : 25 ,
    'city' : {
        'name' : 'Madhubani' ,
        'state' : 'Bihar' ,
        'country' : 'India',
        'pincode' : 847108
    }
}
print(f"Dictionary itmes are : {my_dict}") 

for key , value in my_dict.items() :
    print(f" dictionary key is :{key} and value is : {value}")
    print(f"Length of dictionary is : {len(my_dict)}")

city = my_dict['city']

print(f"city details are : {city}")



# Summary : -- 
# 1. List are used to store multiple items in a single variable and are mutable , while tuples are used to store mutiple items in a single variable and are immutable , 
# 2. Dictionaries are used to store key-value pairs and are mutable .
# 3. List are defined using square brackets [] , tuples are defined using parentgheses () , and dictionaries are defined using curly braces {} .

