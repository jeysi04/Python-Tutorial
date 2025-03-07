#Finding area of square, circle and rectangle
print("Please pick what shape your polygonn is:")
print("1) Square")
print("2) Rectangle")
print("3) Circle")

ans = float(input("Answer: "))

if(ans == 1):
    side = float(input("\nPlease input the length of one side: "))
    area = float(side * side)
    print("\nThe area of the square is", area)
elif(ans == 2):
    length = float(input("\nPlease input the length of the rectangle: "))
    width = float(input("Please input the width of the rectangle: "))
    area = float(width * length)
    print("\nThe area of the rectangle is ", area)