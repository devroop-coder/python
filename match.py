# a = int(input("Enter a number: "))
# match a:
#     case 0 : print("Zero")
#     case _ : print ("Other than zero")
age = int(input("Enter your age: "))

match age :
    case 18 : print("You are 18 years old")
    case _ : print ("NOt found")