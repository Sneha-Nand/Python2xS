# Enter three sides of triangle and find if triangle is equilateral, isoscles or scalene traingle

s1 = float(input("Enter first side of trianble") )
s2 = float(input("Enter second side of triangle"))
s3 = float(input("Enter third side of triangle"))

if s1==s2==s3:
    print("Triangle is equilateral")
elif s1==s2 or s1==s3 or s2==s3:
    print("Triangle is isoscles")
else:
    print("Triangle is scalene")