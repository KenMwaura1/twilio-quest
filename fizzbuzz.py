import sys

yx = sys.argv
yx.pop(0)


for i in yx:
    i = int(i)
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)




