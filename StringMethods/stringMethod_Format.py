#String Methods: format , we can use positional arguments or keyword arguments to specify the order
import socket
import os

try: 
    hostName = socket.gethostname()
    print(hostName)
    ipaddress = socket.gethostbyname(hostName)
    print(ipaddress)
    pingCmd = '{0} "{2}"'.format('ping', 't', ipaddress) #can move the variable assignment
    print(pingCmd)
    consoleout = os.popen(pingCmd).read()
    # another = ''''%s' --"%s" "%s"'''%('ping','t', ipaddress) #variable is fixed and appears in same order as it is defined. 
    # print(another)

except Exception as e:
    print(e)