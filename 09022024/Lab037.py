# Program to find the maximum of 3 nos
#
# a = 10
# b = 20
# c = 30
#
# if a>b and a>c:
#     print("a is greater")
# elif b>a and b>c:
#     print("b is breater")
# elif c>a and c>b:
#     print("c is greater")
#
# # Take input from user
#
no1 = int(input("Enter number 1"))
no2 = int(input("Enter number 2"))
no3 = int(input("Enter number 3"))
#
# if no1>no2 and no1>no3:
#     print("Max is", no1)
# elif no2>no1 and no2>no3:
#     print("Max is",no2)
# else:
#     print("Max is", no3)

# using max function

max_num = max(no1, no2, no3)
print(max_num)
