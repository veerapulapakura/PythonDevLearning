
#Write a program which can compute the factorial of a given numbers.

n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)