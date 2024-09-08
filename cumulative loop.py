#cumulative loop

"""
sum = 0 
for i in range(1,11):
    sum = sum + (i*i)
print("sum of first 10 squares is", sum)
"""
#C:\Users\User\Documents\Python Tutorial
import os 
input_path = input("enter the directory path")
print(input_path)
if os.path.exists(input_path):
    sum = 0 
    for efile in os.listdir(input_path):
        # print(efile)
        fullpath = os.path.join(input_path, efile)
        print(fullpath)
        filesize = os.path.getsize(fullpath)
        print(filesize)
        sum  += filesize
        
    print("size of the %s is %d"%(input_path,sum))
else:
    print("Entered path %s doesnt exist"%input_path)

