# function definition
'''
syntax:
    def functionName(args):
        statement
        return variableName
'''
""" fist function to print a simple line """


def functionPrint():
    print("This is just a simple print function")


""" transfer a variable into funciton"""


def invokeVariable(str1):
    print(str1)


""" function with return value """


def functionReturn(str1, str2):
    return "first args is {}, second args is {}".format(str1, str2)


"""transfer a collection into function """


def functionArgsAndKwargs(*args, **kargs):
    print("args is {}".format(args))
    print("kwargs is {}".format(kargs))


functionPrint()

strArg = "transfer variable to function"
print("type of string is : {}".format(type(strArg)))

invokeVariable(strArg)

print(functionReturn("hi", "you"))
print("functionReturn: {}".format(functionReturn))

functionArgsAndKwargs("Dell", "HP", "Samsung", "Apple",
                      color="white", price=31415.9)

brand = ["DELL", "HP", "Samsung", "Apple"]
otherInfo = {'color': 'white', 'price': 31415.9}

# if do not use * then all arguments will cast in to collection 所有的参数都会转化为集合而成为args参数，而keyword参数则会因为没有赋值而成为空的dic字典类型
functionArgsAndKwargs(brand, otherInfo)

functionArgsAndKwargs(*brand, **otherInfo)
