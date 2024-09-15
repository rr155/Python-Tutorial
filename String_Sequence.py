#Sequence Container and Collection Framework
#collection is storing of data
# sequence data type --> stores several object, each object has an order and object can be referred by
#  an index 

tempstring = "Welcome to Elegant123!#"
# print(tempstring[-3:])
# print(tempstring[::50])

digitCount= charCount= otCount = 0
cc = 0

for ec in tempstring:
    if ec.isalpha():
        charCount +=1
    elif ec.isdigit():
        digitCount +=1
    else :
        otCount +=1

print(digitCount, charCount, otCount)

print(dir(digitCount))
# del digitCount #del deletes the variable 
# print(digitCount)

for index, value in enumerate(tempstring):
    print(index, value)
    
print(enumerate(tempstring))
