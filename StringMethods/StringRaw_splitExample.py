# r in front of string puts it in Raw format and doesnt do any \ unicode methods. 
tempString = r"C:\\Personal\pythonScript\python-ppt\TechTra\ContinueLoop.log"

print(tempString)

print(tempString.split('\\'))
print(tempString.split('\\')[-1])

print(tempString.replace('py','cust'))