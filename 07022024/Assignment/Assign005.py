# Program to take two numbers as input and compare both numbers and print greater than , less than or equal to

No1 = int(input("Enter First Number :"))
No2 = int(input("Enter Second number :"))

# print( (No1 > No2), No1, "is greater than", No2)
# print( (No1 < No2 ), No1 , "is less than " , No2)
# print((No1 <= No2 ), No1 , "is equal to ", No2)

if (No1>No2):
    print(No1, "is greater than ", No2)
elif (No1<No2):
    print(No1, "is less than ", No2)
elif (No1 <= No2 ):
    print(No1 , "is equal to ", No2)


