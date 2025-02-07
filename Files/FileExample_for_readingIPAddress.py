import os

def IpCollect():
    try:
        filePath = os.getcwd()
        print (filePath)
        fp = os.path.join(filePath,'testFile.txt')
        print (fp)
        if os.path.exists(fp):
            fobj1 = open('result_writelist_0302.txt','w')
            fobj = open(fp,'r')
            content = fobj.readlines()#read,readline,readlines
            print (content)
            resutList = [eLine for eLine in content if eLine.split('.')[-2]=='163']#List comprehension
            fobj1.writelines(resutList)#write a list
            # for eline in content:
            #     if '163' in eline:
            #         fobj1.write(eline)
            fobj.close()
            fobj1.close()

        else:
            print ("File %s is not present in the location"%fp)
    except Exception as e:
        print (e)

IpCollect()
