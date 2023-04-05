import sys


def add(x, y):
    z = int(x) + int(y)
    if z <= 0:
        print("You have chosen the path of destitution.")
    elif z in range(1,101):
        print("You have chosen the path of plenty.")
    else:
        print("You have chosen the path of excess.")
    return z


print(add(sys.argv[1], sys.argv[2]))
