# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#
# Example:
#
# 0100,0011,1010,1001

def check(x):                   # check function returns true if divisible by 5
    return int(x,2)%5 == 0      # int(x,b) takes x as string and b as base from which
                                # it will be converted to decimal
data = input().split(',')

data = list(filter(check,data)) # in filter(func,object) function, elements are picked from 'data' if found True by 'check' function
print(",".join(data))


data = input().split(',')
data = list(filter(lambda i:int(i,2)%5==0,data))    # lambda is an operator that helps to write function of one line
print(",".join(data))