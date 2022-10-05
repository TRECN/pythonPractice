a=[1,2,3]

try:
    #no error part
    print("no err")
    #error part
    print (a[4])
except:
    print("index out of range")