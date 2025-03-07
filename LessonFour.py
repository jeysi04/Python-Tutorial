# Logical Operators
# and, or, not


temp = 30
is_raining = False
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside!")
    print("It is sunny!")
elif temp >= 28 and not is_sunny:
    print("It is hot outside!")
    print("It is cloudy!")
elif temp < 0:
    print("It is cold outside!")
elif temp > 35 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event is still scheduled.")