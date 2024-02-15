# To find if entered year is a leap year

year = int(input("Enter year :"))

# leap_year =

if year % 100 == 0 and year % 400 == 0:
    print("This year is a Leap year")
else:
    print("This is not a leap year")
