#exception handling 
#predict ares where errors can happen then i can use Exception handling to prevent my code to break
# try: 
#     for i in range(1,100):
#         p = i
#         print("p")
# except NameError as eobj:
#     print(eobj)
# except ValueError as eobj1:
#     print(eboj1)
# finally:
#     print("restart")


import traceback

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        print("Entered number is %d"%n)
        break
    except ValueError as e:
        print(traceback.format_exc())
        print("No Valid integer! Please retry again")
    finally:
        print("i will execute no matter what")
