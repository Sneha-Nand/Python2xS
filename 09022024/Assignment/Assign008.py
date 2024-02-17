# Factorial  series
# 5! = 5*4*3*2*1

num1 = int(input("Enter number :"))
print("Number is:")
facto = 1

while (num1 > 0):
    facto = num1 * facto
    num1 = num1 - 1

print(facto)

