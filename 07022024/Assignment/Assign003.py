# Program to calculate area of circle
# we can import pi from math function as well as
import math
#pi = 3.14
radius = float(input("Enter radius of circle"))

#area_of_circle = pi*radius*radius
#area_of_circle = pi* (radius**2)
#area_of_circle = pi * pow(radius,2)   #pow function

area_of_circle = math.pi * pow(radius,2)
print("Area of circle is :" ,area_of_circle )


