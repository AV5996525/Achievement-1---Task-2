#PSUEDO CODE for Task 2
# Display a user greeting for the calculator
#Create a variable to store user's input, at the same time we can invoke a strip function to remove the white spaces before and after.
# Use an if statement to seperate the two possiblities of having either a numeric value or a letter value
#Create our first scenairo by utilizing an if statement and using the isalpha function to filter out an answer with letters and print an error message notifing the user of the incorrect response
#Create our last scenario by utilizing our else statement. Now we will NEST four seperate if statements that will correspond to each of our possible choices from 1 to 4
#We will utilize the import function to call pi within the NESTED if shapeSelection == 1 statement.
#
print("Welcome to the Geometry Calculator")
shapeSelection = input("1. Calculate the Area of a Circle \n2. Calculate the Area of a Rectangle \n3. Calculate the Area of a Triangle \n4. Quit").strip()
if shapeSelection.isnumeric() == False :
    print("Values 1 to 4 only, no letters.")
else :
    shapeSelection = int(shapeSelection)
    if shapeSelection == 1:
        print("C")
    if shapeSelection == 2:
        print("rect")
    if shapeSelection == 3:
        print("triangle")
    if shapeSelection == 4:
        print("quit")
    if shapeSelection <= 1 or shapeSelection >= 5 :
        print("Only values from 1 to 4 are accepted.")
