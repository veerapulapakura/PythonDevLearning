#Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.

n1 = str(input('Enter the first numner  \n '))
n2 = str(input('Enter the second numner  \n '))

print(type(n1))
print(type(n2))

sum = int(n1)+int(n2)
print(sum)

sum = lambda s1,s2 : int(s1) + int(s2)
print(sum("10","45"))      # 55