import re as R

txt = "This is an assignment."
x = R.search("\s", txt)

print("The first white-space character is located in position:", x.start())