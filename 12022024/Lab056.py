# function sum of 2 numbers


# define the function
def sum_of_num( num1 , num2):
    return num1 + num2

# call the function
sum1 = sum_of_num(10,20)
print(sum1)

sum2 = sum_of_num(10.29, 10.20)
print(sum2)

sum3 = sum_of_num("Pramod", "Datta")
print(sum3)

# TypeError: can only concatenate str (not "int") to str
#sum4 = sum_of_num("Pramod" , 20)
#print(sum4)