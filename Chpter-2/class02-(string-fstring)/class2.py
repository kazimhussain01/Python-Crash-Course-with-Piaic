# print Hello-Python-World
print("Hello Python World")

#! print Message
message = "Hello World Python"
print(message)

message = "Hello Python Crash Course World"
print(message)

#! Name Errors When Using Variables
#* nameError = "Name Error When Using Variable"
#* print(namerror)

#! String with Singal & Double quotation  
print("This is a String")
print("This is also a String")

#! String Types Boundries
#! String Types 'string text', "string text", '''string text''', """string text"""

# Double quotation
name: str = "Kazim Hussain"
print(name)
print(type(name))

# Singal quotation
name: str = 'Kazim Hussain'
print(name)
print(type(name))

#! Error Through 
#* message : str = 'Piaic Student Card \n father's name'
#* print(message)

#! Solve Error
message : str = "Piaic Student Card \nFather's Name"
print(message)

#! Convert any special character into simple character, place \ before character
message : str = 'Piaic Student Card \nFather\'s Name'
print(message)

# Example 02
message : str = 'Piaic Student Card \n"Student" Name\"'
print(message)

# Example 03
message : str = '\'Piaic Student Card\' \n\"Student Name"'''
print(message)


name : str = "Kazim Hussain"
fname : str = "Naseer Ahmad"
education : str = "ICS"
age : int = 18

#! Type Casting Error
#* name : str = "Kazim Hussain"
#* fname : str = "Naseer Ahmad"
#* education : str = "ICS"
#* age : int = 18

#* card : str = "PIAIC Student card \nStudent Name: " + name + "\nAge: " + age
#* print(card)

#! Solve Type Casting Error
name : str = "Kazim Hussain"
fname : str = "Naseer Ahmad"
education : str = "ICS"
age : int = 18

card : str = "PIAIC Student card \nStudent Name: " + name + "\nAge: " + str(age)
print(card)

