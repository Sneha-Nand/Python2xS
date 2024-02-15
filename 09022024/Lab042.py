# Program to enter mark of a student and give grade


Marks = int(input("Enter Marks:"))
print("Marks is :", Marks)

if Marks >= 90 and Marks <= 100:
    print("Your grade is A")
elif Marks >= 80 and Marks <= 89:
    print("Your grade is B")
elif Marks >= 70 and Marks <= 79:
    print("Your grade is C")
elif Marks >= 60 and Marks <= 69:
    print("Your grade is D")
elif Marks >= 0 and Marks <= 59:
    print("Your grade is F")
else:
    print("Invalid Input")
