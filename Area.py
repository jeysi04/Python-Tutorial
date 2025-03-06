#Finding area of square, circle and rectangle
print("Please pick what shape your polygonn is:")
print("1) Square")
print("2) Rectangle")
print("3) Circle")

ans = int(input("Answer: "))

if(ans == 1):
    side = int(input("\nPlease input the length of one side: "))
    area = int(side * side)
    print("\nThe area of the square is ", area)
elif(ans == 2):
    length = int(input("\nPlease input the length of the rectangle: "))
    width = int(input("Please input the width of the rectangle: "))
    area = int(width * length)
    print("\nThe area of the rectangle is ", area)