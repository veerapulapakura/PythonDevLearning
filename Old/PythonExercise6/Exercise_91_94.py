# Please write a program which accepts a string from console and print it in reverse order.
#
# Example: If the following string is given as input to the program:*
#
# rise to vote sir

s=input()
s = s[::-1]
print(s)


s = input()
s = ''.join(reversed(s))
print(s)

#  Please write a program which accepts a string from console and print the characters that have even indexes.
#
# Example: If the following string is given as input to the program:

myString = input()
print(myString[::2])


# Please write a program which prints all permutations of [1,2,3]

import itertools
print(list(itertools.permutations([1,2,3])))
print(list(itertools.permutations([1,2,3,4])))

# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs
# among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads = 35
numlegs = 94
solutions=solve(numheads,numlegs)
print(solutions)