#Trying data types


#Python has data taypes but unlike C or Java, we don't need to write the data types beside
# the variable name

#Integer
x = 10
print(x)

#Float
f = 14.24
print(f)

#Strings
name1 = 'Elena Aldeguar'
name2 = "Elene Santos"
print(name1)
print(name2)

#characters
ch = 'A'
print(ch)

# Exercise

item = input("What item would you like to buy? ")
price = float(input("What is the price of the product? "))
quantity = int(input("How many would you like? "))
total = price * quantity
print(f"Your total is Php {total}")