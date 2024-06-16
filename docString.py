def docc ():
    '''This is a doc String. It is like comment but it can be execute. This is valid if decleared in the first line of a function module class etc.'''
    return "Executed"

print(docc())

# To access doc string 

print(docc.__doc__)