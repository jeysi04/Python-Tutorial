#Decision
# If-Else

age = int(input("Enter your age: "))

if(age >= 18):
    print("You are of legal age!")
elif age < 18:
    print("You are not of legal age!")
else:
    print("Invalid input.")
    
response = input("Are you of legal age? (Y/N): ")

if (response == 'Y'):
    print("Congratulations!")
else:
    print("Aww! That is too bad!")
    
# Operator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print("The operator is invalid.")
    
print(f"The result is {result}.")

