
# print 1 to 10
for i in range(1,11):
    if(i==5):
        break
    print(i)
print("Outside the for loop")

# important is break before or after print
print("==================")
for i in range(1,11):
    print(i)
    if(i==5):
        break
print("Outside the for loop")