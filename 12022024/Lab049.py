# Factirial
# n = 5 -> 5*4*3*2*1 = 120


number = int(input("Enter the number \n"))
if number < 0 :
    print( "Fatorial of number less than 0 is not available")
elif number == 0 :
    print("Factorial of number is 0 is 1")
else :
    fact = 1
    for i in range(1,number+1):
        fact = fact * i
print("Factorial is" , fact)
