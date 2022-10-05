a=[1,2,3,4,5]

i=int(input())
try:
    #exception can occur here
    print(a[i])
    #no err
    print("no err")
except IndexError:
    print("index out of range")
