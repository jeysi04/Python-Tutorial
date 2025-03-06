#Practicing the fundamentals in Python

#The function print() can be written with ''/""
print('Hi')
print("Hello")

#Assigning variables
x = 0
print(x)


#other ways to print
#String
first_name = "Jaycee"
print(f"Your name is {first_name}")
print("Your name is", first_name)

#Integer
value = int(3)
print(f"The value is {value}")                                            

#float
floatingvalue = 3.4
print(f"The value of pi is {value}")

# Boolean
is_student = True

#can choose to have no parenthesis
if (is_student):
    print("You are a student.")
else:
    print("You are not a student.")
    
# Typecasting

name = "Jaycee"
age = 20
GWA = 1.75
is_student = True

GWA = int(GWA)
print(GWA) # will print 1 only

age = float(age)
print(age) # with decimal point

# type() will allow you to know what kind of data type the var is

print(name)
name = bool(name)
print(name)
name = ""
name = bool(name)
print(name)