print("choose options a, b or c ")
print("1.area and circumference of a circle")
print("2.area and perimeter of a triangle")
print("3.area and perimeter of a rectangle")
print("4.area and perimeter of a square")
choice=int(input("choose among the choices :"))

from math import pi
if choice ==1:
          radius=float(input("Enter radius of the circle"))
          area=float(pi*radius*radius)
          circumference=float(2*pi*radius)
          print(" area of circle " ,area)
          print("circumference of circle",circumference)
elif choice ==2:
        base=float(input("Enter base of the triangle"))
        height=float(input("Enter the height of the triangle"))
        hypotenuse=float(input("Enter the hypotenuse of the circle"))
        area=float(0.5*base*height)
        perimeter=(base+hypotenuse+hypotenuse)
        print("areaof triangle",area)
        print("perimeter of triangle",perimeter)
elif choice ==3:
        width=float(input("Enter the width of the rectangle"))
        length=float(input("Enter the length of the rectangle"))
        area=float(length*width)
        perimeter=(length+width+length+width)
        print("area of rectangle",area)
        print("perimeter of rectangle",perimeter)
elif choice ==4:
          #input the side (s)
def calculate_perimeter(side):
    # Perimeter of the square
    perimeter = 4 * side
    return perimeter

def calculate_area(side):
    # Area of the square
    area = side ** 2
    return area

# Input the side of the square
side = float(input("Enter the side length of the square: "))

# Calculate the perimeter
perimeter = calculate_perimeter(side)

# Calculate the area
area = calculate_area(side)

# Display the results
print(f"The perimeter of the square is: {perimeter}")
print(f"The area of the square is: {area}")
else:
        print("invalid option choose 1,2,3 or 4")
