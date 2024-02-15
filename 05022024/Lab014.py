# Strings
# A Bunch of char
# "" or ''
# if there is special characher then we need to use raw string (r infront of String)
# this will be used in th directory path
# format string f

name = "Pramod"
name1 = 'Pramod'

print(name)
print(name1)

print(type(name))
print(type(name1))

dir = "C://abc.txt"
print(dir)

dir1 = 'C://abc.txt'
print(dir1)

dir2 = "C:\abc\abc.txt" # /a has special meaning
print(dir2)

dir3 = "C:\abc\abc.txt"  # /a has special meaning
print(dir3)

dir3 = "C:\\abc\\abc.txt"  # use like this for path
print(dir3)

dir4 = "C:\somedir\some dir" # no issue
print(dir4)

dir5 = 'C:\somedir\some dir' # no issue
print(dir5)

# Format sting
first_name = "Amit"
last_name = "Mishra"
print(f"Your first name is {first_name} and last name is {last_name}") # works with single quote also
print(f"Your name is {first_name}  {last_name}")
