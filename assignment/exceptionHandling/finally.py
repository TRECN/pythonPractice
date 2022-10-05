a=[1,2,3,4,5]

i=int(input())
try:
    #exception can occur here
    print(100/i)

    print(a[i])

except IndexError:
    print("index out of range")
except ZeroDivisionError:
    print("Zero Division Error")
#no error
else:
    print("no exception")
finally:
    print("after exception part")
