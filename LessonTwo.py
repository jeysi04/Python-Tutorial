#Indentation in Python

#example in selection
x = 10
if x < 20:
    print(x, 'is less than 20')
    
#Without the identation, it would lead to syntax error

# to ask for input, use input() function it will return a String var
#Asking user an input
name = input("Please enter your name: ")
print('Your name is', name)


#Exercise
# Add numbers

numone = input("Please input the first number: ")
numtwo = input("Please input the second number: ")

# sum = numone + numtwo; numbers will be stored as strings

#can also be float
sum = int(numone) + int(numtwo) 

print('The sum is', sum)


#Find the square of a number

number = input("Please input the number: ")
sqr = int(number) * int(number)
print(sqr)

