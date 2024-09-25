# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence
# after sorting them alphabetically.

lst = input().split(',')
lst.sort()
print(",".join(lst))
lst.reverse()
print(lst)


