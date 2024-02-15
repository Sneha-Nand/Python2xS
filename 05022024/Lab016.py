name = "batman"
print(len(name))
print(name[4])
print(name[5])
#print(name[6]) - IndexError: string index out of range
print(name[len(name)-1])

# Strings are immutable, that cannot be changed
# that cannot be modified

string ="Hello"
#string[0] = "P" #TypeError: 'str' object does not support item assignment
string = "Pramod"
print(string)
