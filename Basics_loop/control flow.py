#control flow 

#if executes group of statement only when the condition is true otherwise the statement is skipped 
#if else execute group of statement in if if the condition is trues otherwise it goes to the else block 
#elif requires a condition where as else doesnt table any condition 

# var1 = 12.3
# if type(var1) ==str:
#     print("is a string")
# elif type(var1) == int:
#     print("is a integer")
# else :
#     print("is not string or integer")


#program to find the OS of the system
import platform 
import os 

osidentifier = platform.platform()
# print(osidentifier)

if 'window' in osidentifier.lower():
    # print('system is windows')
    cmdstring = 'ipconfig'
else:
    print('underlying os is linux')
    cmdstring = 'ifconfig'
    
var = os.popen(cmdstring).read()
# print(var)



#one line if statements , structure is if, elif , else 
val = -15 
result = {val > 0: 'Positive', val < 0: 'Negative'}.get(True, "Zero")
# print(result)


#match case - matches only a parameter and uses varios cases for the pattern to be matched in the parmeter. "_" is wildcard character
num = int(input("Enter a number between 1 and 3"))

match num:
    case 1:
        print('one')
    case 2: 
        print('two')
    case 3:
        print('three')
    case 4:
        print('four')
    case _:
        print('please enter number only between 1 and 3')

