#Make sure follow proper format Author date purpose
#
#
#
print("Welcome to the Geometry Calculator")
shapeSelection = input("1. Calculate the Area of a Circle \n2. Calculate the Area of a Rectangle \n3. Calculate the Area of a Triangle \n4. Quit").strip()
if shapeSelection.isalpha() :
    print("Values 1 to 4 only, no letters.")
   

else:
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