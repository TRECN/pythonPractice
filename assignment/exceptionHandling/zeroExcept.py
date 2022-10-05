a=int(input())

try:
    #exception may occur here
    print (100//a)
    #no error part
    print("no err")
except ZeroDivisionError:
    print("ZeroDivisionError")