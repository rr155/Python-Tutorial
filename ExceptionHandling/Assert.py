#assert 
# a= 4 
# b = 0

# print("the value of a/b is:")
# assert b!=0
# print(a/b)
import traceback

def avg(marks):
    assert len(marks)!=0
    return sum(marks)/len(marks)
try: 
    mark1 = []
    print("Average of mark1:", avg(mark1))
except Exception as e:
    # print(traceback.format_exc())
    # # finally:
    # #     print("end")
    pass