#variables - there are 2 global and local variables 
var = [5]
print(id(var))

def fun(var):

    print(id(var))

    for i in var:
        var.remove(i)
        i = i - 2
        var.append(i)
        var= []
        print(id(var))
    return var

print (fun(var) )
print(var)

