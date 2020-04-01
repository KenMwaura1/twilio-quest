# The function accepts INTEGER n as parameter.
import sys

yx = sys.argv
yx.pop(0)


#

def fizzBuzz(yx):
    for i in yx:
        print(i)
        n = int(i) 
        for x in range(1,n+1):
            if x % 3 == 0 and x % 5 == 0:
                print("FizzBuzz")
            elif x % 3 == 0:
                print("Fizz")
            elif x % 5 == 0:
                print("Buzz")
            else:
                print(x)


if __name__ == '__main__':
    yx = [input().strip()]

    fizzBuzz(yx)

    print(yx)
