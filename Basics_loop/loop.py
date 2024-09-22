#loops are used to iterate over a sequence (list, tuple, string) over a certain number of times . 
'''
for x in range(10,0, -2):
    print(x)

'''
# range function takes 3 arguments, start, stop and step. Step if not provided assumed the value of 1 
# var = range(99,0,-1)
# print(type(var))

# for i in var:
#     print(str(i)+" Bottles of beer")
20

# write a program which takes input as channel number start and channel number end. Print Sony if the channel is even. 
# print zee is the channel is odd. And print New if the channel is divisible by 7

'''cnum = int(input("Enter the first channel number:"))
cnum2 = int(input("Enter the last channel number:"))

for var in range(cnum, cnum2):
    if var> 0:
        if var%7 == 0:
            print("News")
        elif var%2 ==0 :
            print("Sony")
        else: 
            print("Channel number %d is zee"%var)
    else:
        print("Channel number %d is not valid"%var)'''

# %d , %s , %f are the replaceable parameters for the values that we want to pass. 
var1 = 20
var2 = 'hello'
var3 = 15.5

# print("this is to test parameters %s%d%f"%(var2,var1,var3))

for var in ('hello world'):
    print(type(var))