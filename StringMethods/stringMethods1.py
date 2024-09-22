#methods dont change the original string value. only result is changed 
try:
     tempString = "welcome to EleganT" 
     print(tempString.capitalize()) # makes first letter as capital in a sentence and every other word letter as small
     print(tempString.lower()) # makes all letters as lower
     print(tempString.upper()) # make all letters as upper 
     print(tempString.count('e')) # number of ocurrance of that character
    #  print(tempString.lower().count('e').upper().count('E'))
     print(tempString.lower().split(' ')[2])
except Exception as e:
     print(e)
