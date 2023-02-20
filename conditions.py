# Declare variables
variable1 = value1
variable2 = value2

# Check a condition using an if statement
if variable1 > variable2:
    print("variable1 is greater than variable2")
    
# Check another condition using an if-else statement
if variable1 < variable2:
    print("variable1 is less than variable2")
else:
    print("variable1 is greater than or equal to variable2")
    
# Check multiple conditions using elif statements
if variable1 == 0:
    print("variable1 is equal to 0")
elif variable1 > 0:
    print("variable1 is greater than 0")
else:
    print("variable1 is less than 0")
    
# Check a condition using a ternary operator
result = "positive" if variable1 > 0 else "non-positive"
print(result)

# Examples
# 1.
# Ask the user to enter a number
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# 2.
# Ask the user to enter the shape
shape = input("Enter the shape (rectangle or triangle): ")

# Check if the shape is rectangle or triangle
if shape.lower() == "rectangle":
    # Ask the user to enter the width and height of the rectangle
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    
    # Calculate the area of the rectangle
    area = width * height
    
    # Print the area of the rectangle
    print("The area of the rectangle is:", area)
    
elif shape.lower() == "triangle":
    # Ask the user to enter the base and height of the triangle
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    
    # Calculate the area of the triangle
    area = 0.5 * base * height
    
    # Print the area of the triangle
    print("The area of the triangle is:", area)
    
else:
    # Print an error message if the shape is not recognized
    print("Error: Shape not recognized. Please enter rectangle or triangle.")