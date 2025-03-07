# Madlibs game
# word game where you create a story by filling in blanks with random words

#time = input("Enter a time: ")
#action = input("Enter a series of action: ")

#print(f"Today I woke up at {time} o' clock.")
#print(f"I was late! I didn't had time to eat and just {action}.")


weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K/L): ")

if unit == 'K':
    weight *= 2.205
    print(f"Your weight is {round(weight, 1)}{unit}")
elif unit == 'L':
    weight /= 2.205
    print(f"Your weight is {round(weight, 1)}{unit}")
else:
    print("Invalid unit.")
