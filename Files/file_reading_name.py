import traceback

def fileReadFun():
    try:
        fobj = open('testFile1.txt','r')
        fobj1 = open('result_read_name.txt', 'w')
        fobj1.write('Name'+','+'courseopted'+','+'mobilenumber'+'\n')
        content = fobj.readlines()
        # print(content)
        for eline in content:
            print(eline)
            if eline.strip().split(',')[1].lower()=='python':
                #name = eline.split(',')[0]
                fobj1.write(eline)
            print(eline)
        
    except Exception as e:
        print(traceback.format_exc())

    finally:
        fobj.close()
        fobj1.close()

fileReadFun()