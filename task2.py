#PSUEDO CODE for Task 2
# Display a user greeting for the calculator
#Create a variable to store user's input, at the same time we can invoke a strip function to remove the white spaces before and after.
# Use an if statement to seperate the two input possiblities of having either a numeric value or a letter value
#Create our first scenairo by utilizing an if statement and using the isnumeric function set to FALSE to search the input given to us by the user. This will eliminate the possibility of having the user enter a letter, number, or combination of both.
#Create our last scenario by utilizing our else statement. We need to call the integer function to the user's input, to convert the input into a valid integer value. 
# Now we will NEST four seperate if statements that will correspond to each of our possible choices from 1 to 4 within our else statement.
#We will utilize the import function to assign pi to a variable called "pi" within the NESTED if shapeSelection == 1 statement.
#We will create a nested if statement within our initial else statement to display an error message to the user, if the user's input is not 1,2,3, or 4.
print("Welcome to the Geometry Calculator")
shapeSelection = input("1. Calculate the Area of a Circle \n2. Calculate the Area of a Rectangle \n3. Calculate the Area of a Triangle \n4. Quit").strip()
if shapeSelection.isnumeric() == False :
    print("Values 1 to 4 only, no letters.")
else :
    shapeSelection = int(shapeSelection)
    if shapeSelection == 1:
        import math
        pi = (math.pi)
        cirDiam = float(input("Enter the diameter of the circle:"))
        cirRad = (cirDiam/2)
        cirCircum = (pi*2*cirRad)
        cirArea = (pi)*(cirRad**2)
        print("The circumfrence is" + str(cirCircum) + " cm." + " The area of circle is " + str(cirArea) + " cm².") 
    if shapeSelection == 2:
        rectWidth = float(input("Enter width of rectangle"))
        rectLength = float(input("Enter length of rectangle"))
        rectPerm = ((2*rectWidth)+(2*rectLength))
        rectArea = (rectWidth*rectLength)
        print("The perimeter of the rectangle is " + str(rectPerm) + " cm." + " The area of the rectangle is " + str(rectArea) + " cm².")
    if shapeSelection == 3:
        triWidth = float(input("Enter the triangle base"))
        triLength = float(input("Enter the triangle height"))   
        triSideA = float(input("Enter the first length of the triangle"))
        triSideB = float(input("Enter the second length of the triangle"))
        triSideC = float(input("Enter the third length of the triangle"))
        triArea = ((triWidth*triLength)/2)
        triPerm = (triSideA + triSideB + triSideC)
        print("The perimeter of the triangle is " + str(triPerm) + " cm." + " The traingle area is " + str(triArea) + " cm².")
    if shapeSelection == 4:
        print("Have a great day, please come back again")    
        exit 
    if shapeSelection <= 1 or shapeSelection >= 5 :
        print("Only values from 1 to 4 are accepted.")