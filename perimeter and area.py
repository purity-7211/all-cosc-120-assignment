print("choose options a, b or c ")
print("1.area and circumference of a circle")
print("2.area and perimeter of a triangle")
print("3.area and perimeter of a rectangle")
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

else:
        print("invalid option choose 1,2 or 3")
