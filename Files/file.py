#file is a named location in disk
#file --> to do any operation we need to open the file. ONce its done we close the file.
#Locate --> Open --> read/write operations --> close 
fobj = open(r'c:\Users\User\Documents\Python Tutorial\Files\testFile.txt', 'r') 
fobj1 = open('resultIp_16_11.txt', 'w')

# content = fobj.read() # read entire file 
# content = fobj.readline() # read only first line
content = fobj.readlines()  #read all the lines and stores in a list 
# print(content)

rList = []
for eL in content:
    if int(eL.split('.')[2]) == 165:
        rList.append(eL)

fobj1.writelines(rList)

# print(fobj1.read())

fobj1.close()
fobj.close()