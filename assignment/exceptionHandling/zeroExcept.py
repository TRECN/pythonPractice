a=int(input())

try:
    #exception may occur here
    print (100//a)
except ZeroDivisionError:
    print("ZeroDivisionError")
#no error part
else:
    print("no err")