# Develop a Python script that calculates the square and cube of a given number.
import math
Num = int(input("Enter number:"))

# square_num = Num * Num
# cube_num = Num * Num * Num

# print("Square of a number is :",  square_num)
# print("Cube of a number is" , cube_num)

# Another way using pow
#
# s1 = pow(Num,2)
# c1 = pow(Num,3)
#
# print("Square of a number is :",  s1)
# print("Cube of a number is" , c1)

# Using math library
s2 = Num**2
print(s2)
square_root= math.sqrt(64)
print(square_root)
cube_root = math.cbrt(64)
print(cube_root)