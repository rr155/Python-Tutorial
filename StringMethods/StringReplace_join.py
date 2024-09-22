# Replace first argument is the string to replace, 2nd argument is string with which to replace and 3rd argument is number of 
# occurance. If not passed by default it replaces every occurance 


tempString = r"C:\Personal\pythonScript\python-ppt\TechTra\ContinueLoop.log"

print(tempString.replace('py', 'cust', 1))

print('**'.join(tempString)) # every single character is getting joined with **

tempString = tempString.split('\\')

print("**".join(tempString)) # every list value is joined with ** and output is a string 

print('\\'.join(tempString)) # join is the reverse of split. We can achieve the same thing using join which was previous to split