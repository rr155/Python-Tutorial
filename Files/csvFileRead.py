
filePath = r'C:\Users\KUMBU PANDA\Documents\Learning\Projects\Python-Tutorial\Files\filename_size_03_02.csv'

def csvRead(filePath):
    writePath = '\\'.join(filePath.split('\\')[:-1])
    print (writePath)
    fobj = open(filePath,'r')#Open csv and creata instace of the fobj
    fobj1 = open(writePath+'\\'+'Result_file.csv','w')
    fobj1.write('FilePath'+','+'Size'+'\n')

    contentList = fobj.readlines()#reads all the line and stores in a list
    #print contentList#each item of the list will be ach row of the file
    for eachLine in contentList[1:]:
        eachLine = eachLine.strip('\n')
        #print eachLine.split(',')[-1]
        if int(eachLine.split(',')[-1])<=500:
            print (eachLine)
            fobj1.write(eachLine+'\n')
    fobj.close()
    fobj1.close()

csvRead(filePath)




